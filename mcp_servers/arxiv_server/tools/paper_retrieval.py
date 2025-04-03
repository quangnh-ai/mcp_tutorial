from langchain_community.retrievers import ArxivRetriever

retriever =  ArxivRetriever(
    load_max_docs=1,
    get_ful_documents=True,
)

def get_arxiv_papers(query: str):
    data = retriever.invoke(query)
    return data
