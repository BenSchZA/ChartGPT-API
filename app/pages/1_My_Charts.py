import streamlit as st
from firebase_admin import firestore
import plotly.io as pio
from google.cloud.firestore_v1.base_query import FieldFilter

import app
from app.components.sidebar import Sidebar
from app.auth import Login
from app.utils import copy_url_to_clipboard


# Clear prior query
st.session_state.question = ""

# Check user authentication
login = Login()
user_id = st.session_state.get("user_id", None)

# Display app name
PAGE_NAME = "My Charts"
st.markdown("# " + PAGE_NAME + " 🎨")
st.markdown("### Latest 10 charts generated by you")

# Initialise Streamlit components
sidebar = Sidebar()

charts = app.db_charts.where(
    filter=FieldFilter("user_id", "==", user_id)
).order_by(
    "timestamp", direction=firestore.Query.DESCENDING
).limit(10).stream()

for chart in charts:
    st.markdown(f"#### {chart.get('query_metadata')['query']}")
    st.markdown(f"Dataset: `{chart.get('query_metadata')['dataset_id']}`")
    st.button('Copy chart URL', type="primary", key=chart.id, on_click=copy_url_to_clipboard, args=(f"/?chart_id={chart.id}",))
    
    chart_json = chart.to_dict()["json"]
    fig = pio.from_json(chart_json)
    st.plotly_chart(fig, use_container_width=True)
