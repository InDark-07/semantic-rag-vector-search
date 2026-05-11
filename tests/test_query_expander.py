from app.query_expander import QueryExpander


def test_query_expansion():
    expander = QueryExpander()

    query = "How does the system handle peak load?"

    expanded = expander.expand_query(query)

    assert "horizontal scaling" in expanded