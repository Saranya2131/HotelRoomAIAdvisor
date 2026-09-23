 AI Based Hotel Room Selection Advisor

**Project Description**

Hotel Room AI Advisor is an AI-powered hotel room recommendation system that helps users find a suitable room based on their personal preferences. Users can describe their requirements in natural language, such as budget, preferred view, quietness, and room size.The system uses LangChain and Groq LLM to understand the user's request and extract structured hotel preferences. A Fuzzy Logic-based inference system then evaluates the available rooms using factors such as budget, view, quietness, and space.
Each room receives a suitability score from 0 to 100, and the system displays room recommendations along with price, rating, and suitability score. The application is developed using Python and Streamlit and provides a simple and interactive interface for hotel room selection.

**Problem Statement**

Choosing a suitable hotel room can be difficult because users may have different requirements such as budget, room view, quietness, and room size.

This project provides an AI-based hotel room selection system where users can describe their requirements in natural language. The system understands the requirements using an LLM and uses Fuzzy Logic to calculate the suitability of available hotel rooms.

---

 **Objectives**

- Understand hotel room requirements written in natural language.
- Extract user preferences using an AI/LLM.
- Evaluate hotel rooms using Fuzzy Logic.
- Calculate a suitability score for each room.
- Recommend a suitable hotel room to the user.
- Provide a simple and user-friendly web interface.
- Deploy the application online.

---

 **Technologies Used**

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

 **AI/LLM Component**

The project uses **LangChain with a Groq-hosted Large Language Model (LLM)**.

The LLM processes the user's natural-language request and extracts:

- Budget
- View preference
- Quietness preference
- Room-space preference

 Example Input

I need a quiet room under ₹5000 with a good view and a large room.

**Fuzzy Logic Component**

The project uses a genuine **Fuzzy Inference System** using the `scikit-fuzzy` library.

The system performs:

1. Fuzzification
2. Fuzzy rule evaluation
3. Aggregation
4. Defuzzification
5. Suitability score calculation

The final suitability score is calculated on a scale of **0 to 100**.

---

**Membership Functions**

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

**Fuzzy Rules**

The system uses multiple fuzzy rules to evaluate room suitability.

IF budget is high
AND view is high
AND quietness is high
THEN suitability is excellent

**System WorkFlow**

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

 **How to Run**

Installation / Setup

Follow these steps to run the Hotel Room AI Advisor on your local system.

1. Clone the Repository
git clone https://github.com/Saranya2131/HotelRoomAIAdvisor

cd HotelRoomAIAdvisor

3. Create a Virtual Environment

python -m venv venv
Activate the virtual environment on Windows:
venv\Scripts\activate

3. Install Required Libraries

pip install -r requirements.txt

4. Configure the Groq API Key

Create a .env file in the project folder:

GROQ_API_KEY=your_groq_api_key

Note: Do not upload the .env file or API key to GitHub. Add .env to .gitignore.

5. Run the Application

streamlit run app.py

The application will open in your browser, usually at:

http://localhost:8501

6. Use the Application

Enter a request such as:

I need a quiet room under ₹5000 with a good view and a large room.

Click Find My Room to view the extracted preferences, room recommendations, suitability scores, and recommended room.

**GitHub Repository:**

https://github.com/Saranya2131/HotelRoomAIAdvisor

 Deployment

The application is hosted using **Streamlit Community Cloud**.

**Live Application:**

https://hotelroomaiadvisor-6czewqvpsfqqqr77lwgeaj.streamlit.app
