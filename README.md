# 🛒 Multi-Agent RAG E-commerce Support Resolution Agent

## 📌 Overview

This project implements a **multi-agent Retrieval-Augmented Generation (RAG) system** for resolving e-commerce customer support tickets using policy documents.

The system ensures responses are:

* ✅ Policy-grounded
* ✅ Citation-backed
* ✅ Safe and compliant
* ❌ Free from hallucinations

---

## 🚀 Key Features

* 🔍 **RAG Pipeline** (FAISS + Embeddings)
* 🤖 **LLM-based Response Generation** (FLAN-T5)
* 🧩 **Multi-Agent Architecture**

  * Triage Agent
  * Policy Retriever
  * Resolution Generator
  * Safety / Compliance Agent
* 📎 **Citation Enforcement**
* ⚠️ **Hallucination Control (rule + prompt based)**

---

## 🏗️ Architecture

```text
User Query + Order Context
        ↓
   Triage Agent
        ↓
Policy Retriever (FAISS)
        ↓
Resolution Generator (LLM)
        ↓
Safety / Compliance Agent
        ↓
 Final Structured Output
```

---

## 🧠 How It Works

1. **Triage Agent**

   * Classifies issue type (return, refund, shipping, etc.)
   * Identifies missing information

2. **Policy Retriever**

   * Fetches relevant policy chunks from vector database

3. **Resolution Generator**

   * Uses LLM (FLAN-T5) + rule-based logic
   * Produces structured, grounded response

4. **Safety Agent**

   * Validates:

     * citation presence
     * correct format
     * no unsupported claims

---

## 📂 Project Structure

```text
src/
│
├── retriever.py   # FAISS vector retrieval
├── agents.py      # triage, generation, safety agents
├── main.py        # pipeline execution
```

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* HuggingFace Transformers (FLAN-T5)
* Sentence Transformers (MiniLM Embeddings)

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the system

```bash
python src/main.py
```

---
🚀 Setup & Run Instructions

git clone https://github.com/ArhamBabel/multi-agent-rag-ecommerce-support.git
cd multi-agent-rag-ecommerce-support
pip install -r requirements.txt

# Add your API key in a .env file
OPENAI_API_KEY=your_api_key

# Run the project
python main.py

## 📥 Input Format

### Ticket (example)

```text
"My order arrived damaged. Can I return it after 5 days?"
```

### Order Context (example)

```python
{
  "order_status": "delivered",
  "delivery_date": "5 days ago",
  "item_category": "general",
  "shipping_region": "India"
}
```

---

## 📤 Output Format

```text
Classification: return (confidence: 0.9)

Clarifying Questions:
- None

Decision: deny

Rationale:
Damaged items must be reported within 48 hours, but 5 days exceeds this limit.

Citations:
- If a customer receives a damaged item, they must report it within 48 hours of delivery.

Customer Response:
Dear Customer,
Based on our policy, damaged items must be reported within 48 hours, and your request exceeds this timeframe.

Next Steps:
- Contact support for further clarification if needed.
```

---

## 📊 Evaluation

The system was evaluated on **20 support tickets**, including:

* Standard cases (returns, refunds, shipping)
* Exception cases (damaged items, non-returnable products)
* Ambiguous queries (missing information)
* Out-of-policy requests

### Results:

* ✅ Citation Coverage: ~100%
* ✅ Unsupported Claim Rate: ~0%
* ✅ Escalation / Safety Handling: Effective

### Example Scenarios:

* Damaged item after deadline → correctly denied
* Missing item → refund guidance provided
* Out-of-policy request → safe response generated

---

## ⚠️ Limitations

* Uses a small LLM (FLAN-T5) → limited reasoning capability
* Rule-based logic required for critical decisions
* Synthetic dataset (not production-scale policies)

---

## 🚀 Future Improvements

* Use larger instruction-tuned models (e.g., Llama, Mistral)
* Improve conflict resolution across policies
* Add UI (Streamlit / Gradio)
* Integrate real-time order data

---

## 👤 Author

Arham

---

## 📌 Notes

This project was developed as part of an AI/ML Engineer Intern assessment, focusing on:

* grounded reasoning
* safe outputs
* multi-agent system design
* practical real-world applicability
