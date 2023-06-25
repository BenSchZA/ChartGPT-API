import chartgpt
from app.config.default import datasets
import pytest


class TestSampleQuestions():
    @pytest.mark.parametrize(
        'dataset, question', [(dataset, question) for dataset in datasets for question in dataset.sample_questions]
    )
    def test_sample_question(self, dataset, question):
        agent = chartgpt.get_agent(dataset_ids=[dataset.id])
        agent.run(input=question)
