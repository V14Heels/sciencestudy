import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Cells & Transport Quiz", page_icon="🧬")

st.title("🧬 Cells & Transport Review")
st.write("Select the best answer for each question below.")
st.markdown("---")

# --- QUIZ DATA ---
questions = [
    {
        "q": "1. Which organelle is responsible for cellular respiration?",
        "options": ["Chloroplast", "Mitochondria", "Nucleus", "Ribosome"],
        "correct": "Mitochondria",
        "note": "Mitochondria is the 'powerhouse' where respiration happens."
    },
    {
        "q": "2. Which scientist was the first to see a LIVING cell?",
        "options": ["Robert Hooke", "Theodor Schwann", "Matthias Schleiden", "Anton van Leeuwenhoek"],
        "correct": "Anton van Leeuwenhoek",
        "note": "Leeuwenhoek used a microscope to see living cells."
    },
    {
        "q": "3. What is the movement of particles from High to Low density called?",
        "options": ["Osmosis", "Diffusion", "Active Transport", "Endocytosis"],
        "correct": "Diffusion",
        "note": "Diffusion is the general movement from High to Low."
    },
    {
        "q": "4. The diffusion of WATER across a membrane is specifically called:",
        "options": ["Osmosis", "Equilibrium", "Active Transport", "Respiration"],
        "correct": "Osmosis",
        "note": "Osmosis is specifically for WATER."
    },
    {
        "q": "5. Active Transport is different from Passive Transport because:",
        "options": ["Active transport requires energy", "Active transport moves water only", "Passive transport requires energy", "Passive transport produces ATP"],
        "correct": "Active transport requires energy",
        "note": "Active transport requires ATP (energy)."
    },
    {
        "q": "6. What are the products of Photosynthesis?",
        "options": ["Carbon Dioxide and Water", "Glucose and Oxygen", "ATP and Carbon Dioxide", "Lactic Acid and Energy"],
        "correct": "Glucose and Oxygen",
        "note": "Plants make Glucose (sugar) and Oxygen."
    },
    {
        "q": "7. If a human body cell has 46 chromosomes, how many does a sex cell have?",
        "options": ["46", "92", "23", "12"],
        "correct": "23",
        "note": "Sex cells (sperm/egg) have half the chromosomes (23)."
    },
    {
        "q": "8. What happens during Cytokinesis?",
        "options": ["DNA is copied", "Chromosomes line up", "Cytoplasm separates into two cells", "Nucleus disappears"],
        "correct": "Cytoplasm separates into two cells",
        "note": "Cytokinesis is the final split of the cytoplasm."
    },
    {
        "q": "9. Which phase of mitosis involves chromosomes lining up in the MIDDLE?",
        "options": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "correct": "Metaphase",
        "note": "M for Middle = Metaphase."
    },
    {
        "q": "10. Which phase of mitosis involves chromosomes being pulled APART?",
        "options": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "correct": "Anaphase",
        "note": "A for Apart = Anaphase."
    },
    {
        "q": "11. A solution with the MOST solute (compared to the cell) is called:",
        "options": ["Isotonic", "Hypotonic", "Hypertonic", "Equitonic"],
        "correct": "Hypertonic",
        "note": "Hyper = High solute."
    },
    {
        "q": "12. Who concluded that all PLANTS are made of cells?",
        "options": ["Schleiden", "Schwann", "Virchow", "Hooke"],
        "correct": "Schleiden",
        "note": "Schleiden studied plants."
    }
]

# --- DRAW QUIZ ---
with st.form("quiz_form"):
    user_answers = {}
    for i, q_data in enumerate(questions):
        st.subheader(q_data["q"])
        # We use a unique key for each question so Streamlit doesn't get confused
        user_answers[i] = st.radio(
            "Select Answer:", 
            q_data["options"], 
            key=f"q{i}", 
            index=None
        )
        st.write("") # Add a little space

    submitted = st.form_submit_button("Submit Quiz")

# --- CHECK RESULTS ---
if submitted:
    st.markdown("---")
    st.header("Results")
    score = 0
    
    for i, q_data in enumerate(questions):
        user_choice = user_answers[i]
        correct_answer = q_data["correct"]
        
        if user_choice == correct_answer:
            score += 1
            st.success(f"✅ Question {i+1}: Correct!")
        else:
            st.error(f"❌ Question {i+1}: Incorrect.")
            st.info(f"The correct answer was: **{correct_answer}**\n\n*Note: {q_data['note']}*")
    
    # Calculate Score
    percentage = int((score / len(questions)) * 100)
    st.metric("Final Score", f"{score}/{len(questions)}", f"{percentage}%")
    
    if percentage == 100:
        st.balloons()
        st.success("🎉 PERFECT SCORE!")
    elif percentage >= 80:
        st.success("Great job! You're ready.")
    else:
        st.warning("Keep studying the notes above!")
