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

▶️ How to Run
1. Clone the repository
      git clone https://github.com/Saranya2131/HotelRoomAIAdvisor
2. Open the project folder
      cd HotelRoomAIAdvisor
3. Create a virtual environment
      python -m venv venv
4. Activate the virtual environment
      Windows:
      venv\Scripts\activate
5. Install the required libraries
      pip install -r requirements.txt
6. Add the Groq API key
      Create a .env file:
      GROQ_API_KEY=YOUR_API_KEY
7. Run the application
      streamlit run app.py

## 🌐 GitHub Repository

**GitHub Repository:**

https://github.com/Saranya2131/HotelRoomAIAdvisor

## 🚀 Deployment

The application is hosted using **Streamlit Community Cloud**.

**Live Application:**

https://hotelroomaiadvisor-6czewqvpsfqqqr77lwgeaj.streamlit.app
