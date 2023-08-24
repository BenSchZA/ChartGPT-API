import io
import plotly.graph_objects as go

from flask import make_response

from api.chartgpt import QueryResult, answer_user_query


def generate_chart(body):
    question = body['question']
    chart_type = body.get('type', 'json')

    if chart_type == 'json':
        # Logic to generate Plotly figure JSON
        query_result: QueryResult = answer_user_query(question)
        if not query_result.chart:
            return {'error': 'Could not generate chart'}, 400
        else:
            return {
                'query': query_result.query,
                'code': query_result.code,
                'chart': query_result.chart
            }, 200
    elif chart_type == 'png':
        # Logic to generate Plotly figure PNG
        figure_json = answer_user_query(question)
        fig = go.Figure(figure_json)

        # Write the figure to a BytesIO object as a PNG
        img_byte_arr = io.BytesIO()
        fig.write_image(img_byte_arr, format="png")
        png_data = img_byte_arr.getvalue()

        response = make_response(png_data)
        response.headers.set('Content-Type', 'image/png')
        return response, 200
