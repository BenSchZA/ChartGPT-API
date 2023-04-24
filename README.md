# NFTfi "AGI"

- [analytics_bot/](analytics_bot/): Code based on https://www.patterns.app/blog/2023/02/07/chartbot-sql-analyst-gpt using OpenAI's davinci LLM directly via the API.
- [analytics_bot_langchain/](analytics_bot_langchain/): LangChain-based BigQuery analytics agent "toolkit" using OpenAI's GPT-3.5-turbo LLM, see [notebooks/bigquery_agent_toolkit.ipynb](notebooks/bigquery_agent_toolkit.ipynb) for a demo. This code has been structured to match the software architecture of LangChain as much as possible, to remain compatible and be able to make PRs back to public repo.

## Development

### Python Environment

Standard CADLabs Python environment using dependencies from [requirements.txt](requirements.txt).

### Secrets and Environment Variables

Make a copy of [.streamlit/secrets.toml.example](.streamlit/secrets.toml.example) to [.streamlit/secrets.toml](.streamlit/secrets.toml) and fill in the relevant variables.

[.streamlit/secrets.toml](.streamlit/secrets.toml) should not be committed to git and is included in the [.gitignore](.gitignore).

#### Google Auth

Wherever Google Auth expects the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to be set to authenticate, we should load the service account info from Streamlit's secrets. We do this to avoid duplicating secrets. In future we may need to make a refactor to this workflow depending on which service we settle on for deployment of applications.

```python
import streamlit as st
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = bigquery.Client(credentials=credentials)
```

### Streamlit

Edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:

Run Streamlit app locally using `streamlit run streamlit_app.py` - open in a browser and edit the code live.

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
