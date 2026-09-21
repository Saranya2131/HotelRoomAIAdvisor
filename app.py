import streamlit as st

from llm_parser import extract_preferences
from hotel_advisor import recommend_rooms


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Hotel Room AI Advisor",
    page_icon="🏨",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: bold;
    margin-top: 25px;
}

.room-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    margin-bottom: 15px;
}

.recommended-card {
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #4CAF50;
    margin-top: 15px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 15px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">🏨 Hotel Room AI Advisor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Find the hotel room that best matches your preferences '
    'using AI and Fuzzy Logic.'
    '</div>',
    unsafe_allow_html=True
)


# =====================================================
# USER INPUT
# =====================================================

st.markdown(
    '<div class="section-title">📝 Tell Us Your Preferences</div>',
    unsafe_allow_html=True
)

user_query = st.text_area(
    "Describe what you are looking for:",
    placeholder=(
        "Example: I need a quiet room under ₹5000 "
        "with a good view and a large room."
    ),
    height=130
)

find_room = st.button(
    "🔍 Find My Room",
    use_container_width=True
)


# =====================================================
# PROCESS REQUEST
# =====================================================

if find_room:

    if not user_query.strip():

        st.warning(
            "⚠️ Please enter your hotel preferences first."
        )

    else:

        try:

            # -----------------------------------------
            # AI EXTRACTION
            # -----------------------------------------

            with st.spinner(
                "🤖 AI is understanding your preferences..."
            ):

                ai_preferences = extract_preferences(
                    user_query
                )


            # Convert AI response to dictionary

            preferences = {
                "budget_per_night":
                    ai_preferences["budget_per_night"],

                "view":
                    ai_preferences["view_preference"],

                "quietness":
                    ai_preferences["room_noise_preference"],

                "space":
                    ai_preferences["room_size_preference"]
            }


            # -----------------------------------------
            # AI PREFERENCES DISPLAY
            # -----------------------------------------

            st.markdown(
                '<div class="section-title">'
                '🤖 AI Extracted Preferences'
                '</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "💰 Budget",
                    f"₹{preferences['budget_per_night']}"
                )

            with col2:

                st.metric(
                    "👀 View",
                    preferences["view"].title()
                )

            with col3:

                st.metric(
                    "🔇 Quietness",
                    preferences["quietness"].title()
                )

            with col4:

                st.metric(
                    "📐 Room Space",
                    preferences["space"].title()
                )


            # -----------------------------------------
            # FUZZY LOGIC
            # -----------------------------------------

            with st.spinner(
                "🧠 Fuzzy Logic is evaluating the rooms..."
            ):

                recommendations = recommend_rooms(
                    preferences
                )


            # -----------------------------------------
            # ROOM RECOMMENDATIONS
            # -----------------------------------------

            st.markdown(
                '<div class="section-title">'
                '🏨 Room Recommendations'
                '</div>',
                unsafe_allow_html=True
            )

            for room in recommendations:

                with st.container(border=True):

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.subheader(
                            f"🛏️ {room['name']}"
                        )

                    with col2:

                        st.write(
                            f"💰 **₹{room['price']} / night**"
                        )

                        st.write(
                            f"⭐ **Rating:** {room['rating']}"
                        )

                    with col3:

                        st.metric(
                            "🎯 Suitability",
                            f"{room['score']:.2f}/100"
                        )


            # -----------------------------------------
            # RECOMMENDED ROOM
            # -----------------------------------------

            best_room = recommendations[0]

            st.markdown(
                '<div class="section-title">'
                '🏆 Recommended Room'
                '</div>',
                unsafe_allow_html=True
            )

            st.success(
                f"""
### 🛏️ {best_room['name']}

💰 **Price:** ₹{best_room['price']} per night

⭐ **Rating:** {best_room['rating']}

🎯 **Suitability Score:** {best_room['score']:.2f}/100

This room received the highest suitability score based
on your budget, view, quietness and space preferences.
"""
            )


            # -----------------------------------------
            # FUZZY LOGIC EXPLANATION
            # -----------------------------------------

            with st.expander(
                "🧠 How does the Fuzzy Logic work?"
            ):

                st.write(
                    "The system compares your preferences "
                    "with the features of every available room."
                )

                st.write(
                    "It uses fuzzy membership functions and "
                    "fuzzy rules to calculate a suitability "
                    "score from 0 to 100."
                )

                st.write(
                    "The room with the highest suitability "
                    "score is displayed as the recommendation."
                )


        except Exception as e:

            st.error(
                "❌ Something went wrong while processing "
                "your request."
            )

            st.exception(e)


# =====================================================
# FOOTER
# =====================================================

st.markdown(
    '<div class="footer">'
    '🏨 Hotel Room AI Advisor | '
    'AI + Fuzzy Logic Mini Project'
    '</div>',
    unsafe_allow_html=True
)