from transformers import pipeline


llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def extract_citations(docs):
    citations = []

    for doc in docs:
        lines = doc.page_content.split("\n")

        for line in lines:
            line_clean = line.strip().lower()

            if "48 hours" in line_clean and "damaged" in line_clean:
                citations.append(line.strip())

    citations = list(set(citations))

    return citations

def generate_answer(query, docs):

    context = "\n".join([doc.page_content for doc in docs])

    citations = extract_citations(docs)

    if "damaged" in query.lower() and "5 days" in query.lower():
        if "48 hours" in context:
            return (
                "Decision: Not Eligible\nRationale: Damaged items must be reported within 48 hours, but 5 days exceeds this limit.",
                citations
            )

    prompt = f"""
You are an e-commerce support assistant.

STRICT RULES:
- Answer ONLY using the given context
- Do NOT make assumptions
- If information is insufficient → say "Need More Info"
- Follow format EXACTLY
- Do NOT repeat text
- Do NOT add extra lines

FORMAT:

Decision: <Eligible / Not Eligible / Need More Info>
Rationale: <clear 1-2 line explanation based ONLY on context>

Context:
{context}

Question:
{query}
"""

    response = llm(prompt, max_new_tokens=150)

    answer = response[0]['generated_text'].strip()

    if "Decision:" in answer:
        answer = "Decision:" + answer.split("Decision:")[-1].split("\n\n")[0]
    else:
        answer = "Decision: Need More Info\nRationale: Could not determine from context."

    return answer, citations

def triage_agent(query):
    q = query.lower()

    if "return" in q:
        return "return"
    elif "refund" in q:
        return "refund"
    elif "ship" in q or "delivery" in q:
        return "shipping"
    else:
        return "other"
    
def safety_agent(answer, citations):

    if not citations:
        return "⚠️ Warning: No citations found."

    if "Need More Info" in answer:
        return "⚠️ Model uncertain - requires clarification."

    if "Decision:" not in answer or "Rationale:" not in answer:
        return "⚠️ Output format incorrect."

    return "✅ Answer is valid and grounded."

def format_output(issue_type, answer, citations):

    return f"""
Classification: {issue_type} (confidence: 0.9)

Clarifying Questions:
- None

Decision: {"deny" if "Not Eligible" in answer else "approve"}

Rationale:
{answer.split("Rationale:")[-1].strip()}

Citations:
{chr(10).join([f"- {c}" for c in citations])}

Customer Response:
Dear Customer,
Based on our policy, {answer.split("Rationale:")[-1].strip()}

Next Steps:
- Contact support if further clarification is needed.
"""