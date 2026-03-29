from retriever import retrieve_docs
from agents import triage_agent, generate_answer, safety_agent
from agents import format_output
if __name__ == "__main__":
    query = "Can I return a damaged item after 5 days?"

    issue_type = triage_agent(query)
    print(f"Issue Type: {issue_type}\n")

    docs = retrieve_docs(query)

    answer, citations = generate_answer(query, docs)

    final_output = format_output(issue_type, answer, citations)
    print(final_output)

    safety = safety_agent(answer,citations)

    print("\nSAFETY CHECK:\n")
    print(safety) 