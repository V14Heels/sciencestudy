import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Cells & Transport Master Quiz", page_icon="🧬")

st.title("🧬 Cells & Transport Master Quiz")
st.write("This quiz covers every topic in your study guide: Scientists, Transport, Photosynthesis, Respiration, and Mitosis.")
st.markdown("---")

# --- QUIZ DATA (Full Comprehensive List) ---
questions = [
    # --- SCIENTISTS ---
    {
        "q": "1. Which scientist was the first to see a LIVING cell?",
        "options": ["Robert Hooke", "Theodor Schwann", "Matthias Schleiden", "Anton van Leeuwenhoek"],
        "correct": "Anton van Leeuwenhoek",
        "note": "Leeuwenhoek used a microscope to see living cells."
    },
    {
        "q": "2. Which scientist concluded that all PLANTS are made of cells?",
        "options": ["Schleiden", "Schwann", "Virchow", "Hooke"],
        "correct": "Schleiden",
        "note": "Schleiden studied plants."
    },
    {
        "q": "3. Which scientist concluded that all ANIMALS are made of cells?",
        "options": ["Schleiden", "Schwann", "Virchow", "Hooke"],
        "correct": "Schwann",
        "note": "Schwann sounds like 'Swan' (an animal)."
    },
    {
        "q": "4. Who stated that all cells come from PREEXISTING cells?",
        "options": ["Schleiden", "Schwann", "Virchow", "Leeuwenhoek"],
        "correct": "Virchow",
        "note": "Virchow added the final part of the Cell Theory."
    },
    
    # --- CELL THEORY ---
    {
        "q": "5. Which of these is NOT part of the Cell Theory?",
        "options": ["All living things are composed of cells", "Cells are the basic unit of life", "All cells have a nucleus", "All cells come from preexisting cells"],
        "correct": "All cells have a nucleus",
        "note": "Prokaryotic cells (like bacteria) do NOT have a nucleus, but they are still cells."
    },

    # --- TRANSPORT ---
    {
        "q": "6. What is the movement of particles from High to Low density called?",
        "options": ["Osmosis", "Diffusion", "Active Transport", "Endocytosis"],
        "correct": "Diffusion",
        "note": "Diffusion is the general movement of particles spreading out."
    },
    {
        "q": "7. The diffusion of WATER across a membrane is specifically called:",
        "options": ["Osmosis", "Equilibrium", "Active Transport", "Respiration"],
        "correct": "Osmosis",
        "note": "Osmosis is specifically the diffusion of WATER."
    },
    {
        "q": "8. Moving large molecules INTO the cell using energy is called:",
        "options": ["Exocytosis", "Endocytosis", "Osmosis", "Diffusion"],
        "correct": "Endocytosis",
        "note": "Endo = Enter (Into the cell)."
    },
    {
        "q": "9. Moving large molecules OUT of the cell using energy is called:",
        "options": ["Exocytosis", "Endocytosis", "Osmosis", "Diffusion"],
        "correct": "Exocytosis",
        "note": "Exo = Exit (Out of the cell)."
    },
    {
        "q": "10. Active Transport is different from Passive Transport because:",
        "options": ["Active transport requires energy", "Active transport moves water only", "Passive transport requires energy", "Passive transport produces ATP"],
        "correct": "Active transport requires energy",
        "note": "Active transport needs ATP energy to move things against the flow."
    },
    {
        "q": "11. What does 'Selectively Permeable' mean?",
        "options": ["Nothing can pass through", "Everything passes through", "Some substances enter, others cannot", "The membrane dissolves"],
        "correct": "Some substances enter, others cannot",
        "note": "The membrane 'selects' what is allowed in."
    },

    # --- SOLUTIONS ---
    {
        "q": "12. A solution with the MOST solute (compared to the cell) is called:",
        "options": ["Isotonic", "Hypotonic", "Hypertonic", "Equitonic"],
        "correct": "Hypertonic",
        "note": "Hyper = High solute (like a hyper kid has high energy)."
    },
    {
        "q": "13. A solution with the LEAST solute is called:",
        "options": ["Isotonic", "Hypotonic", "Hypertonic", "Gin Tonic"],
        "correct": "Hypotonic",
        "note": "Hypo = Low/Under (like hypothermia is low heat)."
    },
    {
        "q": "14. A solution with the SAME amount of solute is called:",
        "options": ["Isotonic", "Hypotonic", "Hypertonic", "Geometric"],
        "correct": "Isotonic",
        "note": "Iso = Equal."
    },

    # --- PHOTOSYNTHESIS & RESPIRATION ---
    {
        "q": "15. In which organelle does Photosynthesis take place?",
        "options": ["Mitochondria", "Nucleus", "Chloroplast", "Ribosome"],
        "correct": "Chloroplast",
        "note": "Chloroplasts contain the green pigment chlorophyll."
    },
    {
        "q": "16. In which organelle does Cellular Respiration take place?",
        "options": ["Mitochondria", "Nucleus", "Chloroplast", "Cell Membrane"],
        "correct": "Mitochondria",
        "note": "The Mitochondria is the powerhouse of the cell."
    },
    {
        "q": "17. What are the REACTANTS (ingredients) for Photosynthesis?",
        "options": ["Glucose & Oxygen", "Carbon Dioxide & Water", "ATP & Water", "Oxygen & Carbon Dioxide"],
        "correct": "Carbon Dioxide & Water",
        "note": "Plants need CO2 and Water (plus sunlight) to start."
    },
    {
        "q": "18. What are the PRODUCTS of Photosynthesis?",
        "options": ["Carbon Dioxide & Water", "Glucose & Oxygen", "ATP & Carbon Dioxide", "Lactic Acid"],
        "correct": "Glucose & Oxygen",
        "note": "Plants produce Sugar (Glucose) and release Oxygen."
    },
    {
        "q": "19. What is the energy source produced in Cellular Respiration?",
        "options": ["Sunlight", "ATP", "Wind", "Heat"],
        "correct": "ATP",
        "note": "Respiration breaks down sugar to create ATP energy."
    },
    {
        "q": "20. Which organisms perform Cellular Respiration?",
        "options": ["Plants only", "Animals only", "All Organisms (Plants & Animals)", "Rocks"],
        "correct": "All Organisms (Plants & Animals)",
        "note": "Both plants and animals need to break down food for energy."
    },

    # --- CELL CYCLE & MITOSIS ---
    {
        "q": "21. What is the correct order of the Cell Cycle phases?",
        "options": ["Interphase, PMAT, Cytokinesis", "PMAT, Interphase, Cytokinesis", "Cytokinesis, Interphase, PMAT", "PMAT, Cytokinesis, Interphase"],
        "correct": "Interphase, PMAT, Cytokinesis",
        "note": "Interphase (growth) -> Mitosis (division) -> Cytokinesis (separation)."
    },
    {
        "q": "22. During which phase does the cell spend most of its time growing and copying DNA?",
        "options": ["Mitosis", "Cytokinesis", "Interphase", "Anaphase"],
        "correct": "Interphase",
        "note": "Interphase is the longest phase of the cell cycle."
    },
    {
        "q": "23. In Mitosis, what happens during METAPHASE?",
        "options": ["Chromosomes appear", "Chromosomes line up in the MIDDLE", "Chromosomes pull APART", "Two nuclei form"],
        "correct": "Chromosomes line up in the MIDDLE",
        "note": "M for Middle = Metaphase."
    },
    {
        "q": "24. In Mitosis, what happens during ANAPHASE?",
        "options": ["Chromosomes appear", "Chromosomes line up in the MIDDLE", "Chromosomes are pulled APART", "Two nuclei form"],
        "correct": "Chromosomes are pulled APART",
        "note": "A for Apart = Anaphase."
    },
    {
        "q": "25. What happens during Cytokinesis?",
        "options": ["DNA is copied", "Nucleus forms", "Cytoplasm divides into two cells", "Chromosomes vanish"],
        "correct": "Cytoplasm divides into two cells",
        "note": "Cytokinesis is the physical splitting of the cell into two."
    },

    # --- MEIOSIS & GENETICS ---
    {
        "q": "26. Mitosis results in:",
        "options": ["2 Identical Daughter Cells", "4 Different Sex Cells", "1 Big Cell", "Dead Cells"],
        "correct": "2 Identical Daughter Cells",
        "note": "Mitosis is for growth and repair (copying body cells)."
    },
    {
        "q": "27. Meiosis results in:",
        "options": ["2 Identical Body Cells", "4 Sex Cells with half chromosomes", "2 Sex Cells", "4 Body Cells"],
        "correct": "4 Sex Cells with half chromosomes",
        "note": "Meiosis creates sperm and egg cells."
    },
    {
        "q": "28. If a human body cell has 46 chromosomes, how many does a Sex Cell have?",
        "options": ["46", "92", "23", "12"],
        "correct": "23",
        "note": "Sex cells have exactly half (23) so they can combine to make 46."
    },

    # --- EXPERIMENTAL VARIABLES ---
    {
        "q": "29. The variable you change ON PURPOSE is the:",
        "options": ["Independent Variable", "Dependent Variable", "Control", "Constant"],
        "correct": "Independent Variable",
        "note": "Independent starts with I. 'I' change it."
    },
    {
        "q": "30. An observation that uses NUMBERS is:",
        "options": ["Qualitative", "Quantitative", "Subjective", "Guess"],
        "correct": "Quantitative",
        "note": "Quantitative = Quantity (Numbers)."
    },
    {
        "q": "31. An observation that uses the FIVE SENSES (no numbers) is:",
        "options": ["Qualitative", "Quantitative", "Subjective", "Math"],
        "correct": "Qualitative",
        "note": "Qualitative describes the Quality (color, smell, texture)."
    }
]

# --- APP LAYOUT ---
with st.form("quiz_form"):
    user_answers = {}
    for i, q_data in enumerate(questions):
        st.subheader(q_data["q"])
        user_answers[i] = st.radio(
            "Select Answer:", 
            q_data["options"], 
            key=f"q{i}", 
            index=None
        )
        st.markdown("---") # Line separator between questions

    submitted = st.form_submit_button("Submit Quiz")

# --- GRADING LOGIC ---
if submitted:
    st.header("📝 Quiz Results")
    score = 0
    
    for i, q_data in enumerate(questions):
        user_choice = user_answers[i]
        correct_answer = q_data["correct"]
        
        if user_choice == correct_answer:
            score += 1
            st.success(f"✅ Question {i+1}: Correct!")
        else:
            st.error(f"❌ Question {i+1}: Incorrect.")
            st.info(f"The correct answer was: **{correct_answer}**\n\n*Explanation: {q_data['note']}*")
    
    # Final Score Display
    st.markdown("---")
    percentage = int((score / len(questions)) * 100)
    st.metric("Final Score", f"{score}/{len(questions)}", f"{percentage}%")
    
    if percentage == 100:
        st.balloons()
        st.success("🎉 PERFECT SCORE! You are 100% ready for the test!")
    elif percentage >= 80:
        st.success("Great job! Review the few you missed and you'll be set.")
    else:
        st.warning("Keep studying! Review the notes above for the questions you missed.")
