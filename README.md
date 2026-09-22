# 🏨 AI Based Hotel Room Selection Advisor

## 📌 Problem Statement

Choosing a suitable hotel room can be difficult because users may have different requirements such as budget, room view, quietness, and room size.

This project provides an AI-based hotel room selection system where users can describe their requirements in natural language. The system understands the requirements using an LLM and uses Fuzzy Logic to calculate the suitability of available hotel rooms.

---

## 🎯 Objectives

- Understand hotel room requirements written in natural language.
- Extract user preferences using an AI/LLM.
- Evaluate hotel rooms using Fuzzy Logic.
- Calculate a suitability score for each room.
- Recommend a suitable hotel room to the user.
- Provide a simple and user-friendly web interface.
- Deploy the application online.

---

## 🛠️ Technologies Used

- **Python**
- **LangChain**
- **Groq LLM**
- **scikit-fuzzy**
- **NumPy**
- **SciPy**
- **NetworkX**
- **Pydantic**
- **Streamlit**
- **Git & GitHub**
- **Streamlit Community Cloud**

---

## 🤖 AI/LLM Component

The project uses **LangChain with a Groq-hosted Large Language Model (LLM)**.

The LLM processes the user's natural-language request and extracts:

- Budget
- View preference
- Quietness preference
- Room-space preference

### Example Input

```text
I need a quiet room under ₹5000 with a good view and a large room.

## 🧠 Fuzzy Logic Component

The project uses a genuine **Fuzzy Inference System** using the `scikit-fuzzy` library.

The system performs:

1. Fuzzification
2. Fuzzy rule evaluation
3. Aggregation
4. Defuzzification
5. Suitability score calculation

The final suitability score is calculated on a scale of **0 to 100**.

---

## 📊 Membership Functions

The project uses triangular membership functions (`trimf`).

### Budget
- Low
- Medium
- High

### View
- Low
- Medium
- High

### Quietness
- Low
- Medium
- High

### Room Space
- Small
- Medium
- Large

### Suitability
- Poor
- Average
- Good
- Excellent

---

## 📐 Fuzzy Rules

The system uses multiple fuzzy rules to evaluate room suitability.

```text
IF budget is high
AND view is high
AND quietness is high
THEN suitability is excellent

### System WorkFlow

User enters hotel requirements
            ↓
       Streamlit UI
            ↓
      LangChain + Groq
            ↓
   AI Preference Extraction
            ↓
 Budget | View | Quietness | Space
            ↓
      Fuzzy Logic System
            ↓
       Fuzzification
            ↓
      Rule Evaluation
            ↓
       Defuzzification
            ↓
     Suitability Score
            ↓
    Room Recommendations
            ↓
      Recommended Room

      