
from analytics_bot_langchain.agents.agent_toolkits import create_bigquery_agent

__all__ = [
    "create_bigquery_agent",
    "run",
]

import pprint
import json
import google.auth
from google.cloud import bigquery
from langchain.chat_models import ChatOpenAI


from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


from analytics_bot_langchain.agents.agent_toolkits import create_bigquery_agent
from analytics_bot_langchain.agents.agent_toolkits.bigquery.utils import get_dataset_ids, get_table_ids, get_tables_summary

pp = pprint.PrettyPrinter(indent=4)
# Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON file that contains your service account key
credentials, _ = google.auth.default(
    scopes=[
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery",
    ]
)
client = bigquery.Client(credentials=credentials)
get_dataset_ids(client=client)
get_table_ids(client=client)
print(json.dumps(get_tables_summary(client=client), sort_keys=True, indent=4))
agent = create_bigquery_agent(ChatOpenAI(temperature=0), bigquery_client=client, verbose=True)


def run(question) -> bool:
    question += ". If it is a plot request, use st.plotly_chart(fig, use_container_width=True) to display the plot at the end"
    agent.run(question)
    return True
