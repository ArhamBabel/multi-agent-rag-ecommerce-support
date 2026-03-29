from retriever import retrieve_docs
from agents import triage_agent, generate_answer, safety_agent
if __name__ == "__main__":
    query = "Can I return a damaged item after 5 days?"

    issue_type = triage_agent(query)
    print(f"Issue Type: {issue_type}\n")

    docs = retrieve_docs(query)

    answer, citations = generate_answer(query, docs)

    print("ANSWER:\n")
    print(answer)

    print("\nCITATIONS:\n")
    for i, c in enumerate(citations):
        print(f"{i+1}. {c.strip()}")

    safety = safety_agent(answer, citations)
    print("\nSAFETY CHECK:\n")
    print(safety)