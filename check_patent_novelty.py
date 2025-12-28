
import os
from dotenv import load_dotenv
from edison_client import EdisonClient, JobNames

def run_patent_search():
    load_dotenv()
    api_key = os.getenv("EDISON_API_KEY")
    if not api_key:
        print("Error: EDISON_API_KEY not found.")
        return

    client = EdisonClient(api_key=api_key.strip())

    # Queries based on the specific claims in the document
    queries = [
        # Claim 1: ht-index governance
        {
            "name": JobNames.PRECEDENT,
            "query": "Has anyone used Head/Tail Breaks (ht-index) as a real-time runtime constraint for Wave Function Collapse (WFC) or other stochastic generative algorithms?"
        },
        {
            "name": JobNames.LITERATURE,
            "query": "What are the latest applications of Bin Jiang's ht-index in generative architectural design or BIM?"
        },
        # Claim 2: HATI Protocol / Tool Universe
        {
            "name": JobNames.PRECEDENT,
            "query": "Are there existing agent-tool protocols that require a 'Topological Context Vector' or state-injection to negotiate tool execution fidelity?"
        },
        # Claim 3: Incursive Noetic Weighting
        {
            "name": JobNames.PRECEDENT,
            "query": "Has the concept of 'Incursive Noetic' weighting been applied to entropy reduction algorithms like Wave Function Collapse?"
        },
        # Claim 4: Hypergraphs in BIM
        {
            "name": JobNames.LITERATURE,
            "query": "What are the state-of-the-art uses of Hypergraphs or Neutrosophic graphs for representing ambiguous relationships in Building Information Modeling (BIM)?"
        }
    ]

    print(f"Running {len(queries)} patent novelty checks...")
    responses = client.run_tasks_until_done(queries)

    for i, response in enumerate(responses):
        print(f"\nQUERY {i+1}: {queries[i]['query']}")
        print(f"TYPE: {queries[i]['name']}")
        print("-" * 40)
        if response.has_successful_answer:
            print(response.answer)
        else:
            print("No clear answer found.")
        print("=" * 40)

if __name__ == "__main__":
    run_patent_search()
