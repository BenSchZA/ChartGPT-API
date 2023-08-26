import streamlit as st
from firebase_admin import firestore
import plotly.io as pio

from app import db_charts
from app.utils import copy_url_to_clipboard
from app.components.notices import Notices


# Show notices
Notices()

# Clear prior query
st.session_state.question = ""

# Display app name
PAGE_NAME = "Chart Gallery"
st.markdown("# " + PAGE_NAME + " 🎨")
st.markdown("### Latest 10 charts generated by users of ChartGPT")

charts = db_charts.order_by(
    "timestamp", direction=firestore.Query.DESCENDING
).limit(10).stream()

# Display all charts
for chart in charts:
    st.markdown(f"#### {chart.get('query_metadata')['query']}")
    st.markdown(f"Dataset: `{chart.get('query_metadata')['dataset_id']}`")
    st.button('Copy chart URL', type="primary", key=chart.id, on_click=copy_url_to_clipboard, args=(f"/?chart_id={chart.id}",))
    
    chart_json = chart.to_dict()["json"]
    fig = pio.from_json(chart_json)
    st.plotly_chart(fig, use_container_width=True)
