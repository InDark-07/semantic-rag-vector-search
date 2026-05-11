from app.mocks import MockGenerativeModel


class QueryExpander:
    def __init__(self):
        self.model = MockGenerativeModel("gemini-mock")

    def expand_query(self, query: str):
        expanded_query = self.model.generate_content(query)
        return expanded_query