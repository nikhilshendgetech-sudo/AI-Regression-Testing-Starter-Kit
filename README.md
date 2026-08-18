# AI Regression Testing Starter Kit

A practical starter kit for QA Engineers and SDETs to design repeatable regression testing workflows for AI/LLM applications.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-8%2B-green.svg)](https://pytest.org/)
[![Promptfoo](https://img.shields.io/badge/Promptfoo-LLM%20Evaluation-purple.svg)](https://www.promptfoo.dev/)

---

## 🚀 What is this?

AI applications can change their behavior when prompts, models, retrieval configuration, or application logic changes.

Traditional software regression testing is not always enough for AI-powered applications because the output can vary even when the underlying application code appears unchanged.

This starter kit provides a practical foundation for creating **repeatable AI regression tests**, evaluating responses, and comparing results before releasing changes.

It is designed as a starting point for QA Engineers, SDETs, and developers working with AI/LLM-based applications.

---

## 🎯 Why AI Regression Testing?

AI application quality can be affected by changes to:

* Prompts
* LLM models
* Model parameters
* Retrieval configuration
* RAG pipelines
* Application logic
* System instructions
* Evaluation criteria

A change that improves one scenario can unintentionally degrade another.

AI regression testing helps identify these changes before they reach production.

---

## ✨ What's Included

This starter kit includes:

* 10 practical AI regression test scenarios
* CSV-based evaluation dataset
* AI evaluation scorecard
* Python + pytest testing framework
* Promptfoo evaluation example
* GitHub Actions CI workflow
* Customer Support example
* RAG Assistant example
* Prompt Regression example
* Practical AI testing documentation
* Quick-start documentation
* Reusable testing templates

---

## 🔄 AI Regression Testing Workflow

```text
┌─────────────────────┐
│   AI Application    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Test Dataset      │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Run Evaluation     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Score Responses    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Compare Baseline    │
└──────────┬──────────┘
           ↓
      Regression?
       ↙       ↘
     YES       NO
      ↓         ↓
   Investigate  Release
```

### Testing Process

1. Create a representative evaluation dataset
2. Define expected behavior
3. Establish a baseline
4. Change the prompt, model, retrieval configuration, or application logic
5. Run the same evaluation suite
6. Compare current results with the baseline
7. Investigate any regressions
8. Release only when quality thresholds are satisfied

---

## 📁 Project Structure

```text
AI-Regression-Testing-Starter-Kit/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── datasets/
│   └── AI regression evaluation datasets
│
├── docs/
│   └── AI testing documentation
│
├── examples/
│   ├── customer-support/
│   ├── rag-assistant/
│   └── prompt-regression/
│
├── promptfoo/
│   └── Promptfoo evaluation examples
│
├── python/
│   ├── tests/
│   └── Python regression testing framework
│
├── templates/
│   └── reusable AI testing templates
│
├── CHANGELOG.md
├── README.md
└── .gitignore
```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/nikhilshendgetech-sudo/AI-Regression-Testing-Starter-Kit.git
cd AI-Regression-Testing-Starter-Kit
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r python/requirements.txt
```

### 4. Run the regression tests

```bash
pytest python/tests -v
```

---

## 🧪 Example Scenarios

The starter kit demonstrates different AI testing scenarios.

### Customer Support

Validate whether an AI customer-support assistant:

* Provides relevant responses
* Follows expected behavior
* Avoids inappropriate responses
* Maintains consistent output quality

### RAG Assistant

Validate AI responses in a retrieval-augmented generation workflow.

Typical checks include:

* Relevant information retrieval
* Response correctness
* Context-aware answers
* Handling unsupported questions

### Prompt Regression

Compare AI behavior before and after a prompt change.

This helps identify situations where a new prompt improves one use case but causes regressions in another.

---

## 📊 Evaluation & Results

The project includes evaluation datasets and a scorecard approach for tracking AI response quality.

A typical regression evaluation can compare:

```text
Baseline
   ↓
Run Test Dataset
   ↓
Calculate Evaluation Scores
   ↓
Compare With Current Version
   ↓
Identify Quality Changes
```

Example result categories can include:

| Evaluation Area | Purpose                                               |
| --------------- | ----------------------------------------------------- |
| Correctness     | Is the response factually appropriate?                |
| Relevance       | Does the response address the question?               |
| Consistency     | Does behavior remain stable?                          |
| Safety          | Does the response follow defined safety expectations? |
| Regression      | Did quality decrease after a change?                  |

---

## 🤖 Promptfoo

The repository also includes a Promptfoo-based evaluation example.

Promptfoo can be used to evaluate and compare prompts and LLM outputs across multiple test cases.

The `promptfoo/` directory provides an example setup that can be extended for project-specific evaluations.

---

## 🔁 CI/CD

GitHub Actions is included to automatically execute the regression test suite.

The workflow is located at:

```text
.github/workflows/ci.yml
```

The CI pipeline helps ensure that changes to the testing framework can be validated automatically.

### CI Flow

```text
Developer Change
       ↓
   Git Push
       ↓
GitHub Actions
       ↓
Install Dependencies
       ↓
Run Regression Tests
       ↓
    Test Result
     ↙       ↘
   PASS      FAIL
    ↓          ↓
 Continue    Investigate
```

This provides a foundation for integrating AI regression testing into a larger CI/CD pipeline.

---

## 👥 Who is this for?

This starter kit is useful for:

* QA Engineers
* SDETs
* Automation Engineers
* AI Application Developers
* LLM Application Teams
* RAG Application Teams
* Teams introducing AI quality gates into CI/CD

---

## 🗺️ Roadmap

Future improvements may include:

* [ ] More AI evaluation metrics
* [ ] LLM-as-a-Judge evaluation
* [ ] Automated baseline comparison
* [ ] Quality threshold gates
* [ ] HTML evaluation reports
* [ ] Expanded RAG testing scenarios
* [ ] Additional CI/CD integrations
* [ ] Production-oriented AI test examples

---

## 📚 Documentation

Additional guides and examples are available in:

```text
docs/
examples/
templates/
```

---

## ⭐ Project Goal

The goal of this project is to provide a simple and practical starting point for implementing **repeatable AI regression testing** rather than treating AI testing as a one-time manual activity.

---

## 📄 License

This project is provided for educational and demonstration purposes.
