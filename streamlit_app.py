import time

def run_quiz():
    print("--- COMPREHENSIVE CELLS & TRANSPORT EXAM ---")
    print("This quiz covers the entire study guide.")
    print("Type A, B, C, or D for your answer.")
    print("-" * 50)

    score = 0
    
    # Full list of questions covering every bullet point
    questions = [
        # --- SCIENTISTS ---
        {
            "question": "1. Which scientist was the first to see a LIVING cell?",
            "options": ["A. Robert Hooke", "B. Theodor Schwann", "C. Matthias Schleiden", "D. Anton van Leeuwenhoek"],
            "answer": "D",
            "explanation": "Leeuwenhoek used a microscope to see living cells."
        },
        {
            "question": "2. Which scientist concluded that all PLANTS are made of cells?",
            "options": ["A. Schleiden", "B. Schwann", "C. Virchow", "D. Hooke"],
            "answer": "A",
            "explanation": "Schleiden = Plants."
        },
        {
            "question": "3. Which scientist concluded that all ANIMALS are made of cells?",
            "options": ["A. Schleiden", "B. Schwann", "C. Virchow", "D. Hooke"],
            "answer": "B",
            "explanation": "Schwann = Animals (Sounds like Swan)."
        },
        {
            "question": "4. Who stated that all cells come from PREEXISTING cells?",
            "options": ["A. Schleiden", "B. Schwann", "C. Virchow", "D. Leeuwenhoek"],
            "answer": "C",
            "explanation": "Virchow added the 3rd part of the cell theory."
        },
        # --- CELL THEORY ---
        {
            "question": "5. Which of these is NOT part of the Cell Theory?",
            "options": ["A. All living things are composed of cells", "B. Cells are the basic unit of life", "C. All cells have a nucleus", "D. All cells come from preexisting cells"],
            "answer": "C",
            "explanation": "Not all cells have a nucleus (prokaryotes don't)."
        },
        # --- TRANSPORT ---
        {
            "question": "6. What is the movement of particles from High to Low density called?",
            "options": ["A. Osmosis", "B. Diffusion", "C. Active Transport", "D. Endocytosis"],
            "answer": "B",
            "explanation": "Diffusion is the general movement from High to Low."
        },
        {
            "question": "7. The diffusion of WATER across a membrane is specifically called:",
            "options": ["A. Osmosis", "B. Equilibrium", "C. Active Transport", "D. Respiration"],
            "answer": "A",
            "explanation": "Osmosis is specifically for WATER."
        },
        {
            "question": "8. Moving large molecules INTO the cell using energy is called:",
            "options": ["A. Exocytosis", "B. Endocytosis", "C. Osmosis", "D. Diffusion"],
            "answer": "B",
            "explanation": "Endo = Enter (Into)."
        },
        {
            "question": "9. A solution with the MOST solute (compared to the cell) is:",
            "options": ["A. Isotonic", "B. Hypotonic", "C. Hypertonic", "D. Equitonic"],
            "answer": "C",
            "explanation": "Hyper = High/Over (like a hyper child has high energy)."
        },
        {
            "question": "10. A solution with the LEAST solute is:",
            "options": ["A. Isotonic", "B. Hypotonic", "C. Hypertonic", "D. Gin Tonic"],
            "answer": "B",
            "explanation": "Hypo = Low/Under (like hypothermia)."
        },
        {
            "question": "11. A solution with the SAME amount of solute is:",
            "options": ["A. Isotonic", "B. Hypotonic", "C. Hypertonic", "D. Geometric"],
            "answer": "A",
            "explanation": "Iso = Equal."
        },
        {
            "question": "12. What does 'Selectively Permeable' mean?",
            "options": ["A. Nothing can pass through", "B. Everything passes through", "C. Some substances enter, others cannot", "D. The membrane dissolves"],
            "answer": "C",
            "explanation": "It selects what can get in or out."
        },
         # --- PHOTOSYNTHESIS & RESPIRATION ---
        {
            "question": "13. In which organelle does Photosynthesis take place?",
            "options": ["A. Mitochondria", "B. Nucleus", "C. Chloroplast", "D. Ribosome"],
            "answer": "C",
            "explanation": "Chloroplasts contain chlorophyll for photosynthesis."
        },
        {
            "question": "14. In which organelle does Cellular Respiration take place?",
            "options": ["A. Mitochondria", "B. Nucleus", "C. Chloroplast", "D. Cell Membrane"],
            "answer": "A",
            "explanation": "Mitochondria is the powerhouse."
        },
        {
            "question": "15. What are the REACTANTS (ingredients) for Photosynthesis?",
            "options": ["A. Glucose & Oxygen", "B. CO2 & Water", "C. ATP & Water", "D. Oxygen & CO2"],
            "answer": "B",
            "explanation": "Plants need Carbon Dioxide and Water."
        },
        {
            "question": "16. What are the PRODUCTS of Photosynthesis?",
            "options": ["A. Glucose & Oxygen", "B. CO2 & Water", "C. ATP & Water", "D. Lactic Acid"],
            "answer": "A",
            "explanation": "Plants make Sugar (Glucose) and Oxygen."
        },
        {
            "question": "17. What is the energy source for Cellular Respiration?",
            "options": ["A. Sunlight", "B. ATP", "C. Wind", "D. Heat"],
            "answer": "B",
            "explanation": "Respiration creates ATP energy."
        },
        {
            "question": "18. Which organisms perform Cellular Respiration?",
            "options": ["A. Plants only", "B. Animals only", "C. All Organisms (Plants & Animals)", "D. Rocks"],
            "answer": "C",
            "explanation": "Everything living needs to break down food for energy."
        },
         # --- CELL CYCLE ---
        {
            "question": "19. Which is the correct order of Mitosis?",
            "options": ["A. PMAT", "B. TAM P", "C. PTMA", "D. ATMP"],
            "answer": "A",
            "explanation": "Prophase, Metaphase, Anaphase, Telophase."
        },
        {
            "question": "20. During which phase do chromosomes line up in the MIDDLE?",
            "options": ["A. Prophase", "B. Metaphase", "C. Anaphase", "D. Telophase"],
            "answer": "B",
            "explanation": "M for Middle = Metaphase."
        },
        {
            "question": "21. During which phase are chromosomes pulled APART?",
            "options": ["A. Prophase", "B. Metaphase", "C. Anaphase", "D. Telophase"],
            "answer": "C",
            "explanation": "A for Apart = Anaphase."
        },
        {
            "question": "22. During which phase does the cell spend most of its time growing?",
            "options": ["A. Mitosis", "B. Cytokinesis", "C. Interphase", "D. Anaphase"],
            "answer": "C",
            "explanation": "Interphase is the longest phase."
        },
        {
            "question": "23. What happens in Cytokinesis?",
            "options": ["A. DNA copies", "B. Nucleus forms", "C. Cytoplasm divides into two cells", "D. Chromosomes vanish"],
            "answer": "C",
            "explanation": "Cytokinesis cuts the cell into two."
        },
        # --- MEIOSIS & CHROMOSOMES ---
        {
            "question": "24. Mitosis results in:",
            "options": ["A. 2 Identical Daughter Cells", "B. 4 Different Sex Cells", "C. 1 Big Cell", "D. Dead Cells"],
            "answer": "A",
            "explanation": "Mitosis = Copying body cells."
        },
        {
            "question": "25. Meiosis results in:",
            "options": ["A. 2 Identical Body Cells", "B. 4 Sex Cells with half chromosomes", "C. 2 Sex Cells", "D. 4 Body Cells"],
            "answer": "B",
            "explanation": "Meiosis makes sperm/egg cells with half the DNA."
        },
        {
            "question": "26. If a human body cell has 46 chromosomes, how many does a Sex Cell have?",
            "options": ["A. 46", "B. 23", "C. 92", "D. 12"],
            "answer": "B",
            "explanation": "Sex cells have exactly half (23)."
        },
        # --- SCIENTIFIC METHOD & ORGANS ---
        {
            "question": "27. The variable you change ON PURPOSE is the:",
            "options": ["A. Independent Variable", "B. Dependent Variable", "C. Control", "D. Constant"],
            "answer": "A",
            "explanation": "Independent starts with I. 'I' change it."
        },
        {
            "question": "28. An observation that uses NUMBERS is:",
            "options": ["A. Qualitative", "B. Quantitative", "C. Subjective", "D. Guess"],
            "answer": "B",
            "explanation": "Quantitative = Quantity (Numbers)."
        },
        {
            "question": "29. Which organelle controls the cell and contains DNA?",
            "options": ["A. Vacuole", "B. Nucleus", "C. Cytoplasm", "D. Wall"],
            "answer": "B",
            "explanation": "The Nucleus is the brain of the cell."
        }
    ]

    # Loop through questions
    for i, q in enumerate(questions):
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        
        user_ans = input("Your Answer: ").upper().strip()
        
        if user_ans == q["answer"]:
            print(">>> CORRECT!")
            score += 1
        else:
            print(f">>> INCORRECT. The correct answer was {q['answer']}.")
            print(f"Notes: {q['explanation']}")
        
        time.sleep(1.5) # Pause to let her read the explanation

    # Final Score
    print("\n" + "=" * 50)
    print(f"TEST COMPLETE: You scored {score} out of {len(questions)}.")
    percent = (score / len(questions)) * 100
    print(f"Final Grade: {percent:.1f}%")

    if percent == 100:
        print("PERFECT SCORE! You are going to ace the real test!")
    elif percent >= 80:
        print("Great job! Review the few you missed and you'll be set.")
    else:
        print("Good practice. Run this script again to improve your score!")

if __name__ == "__main__":
    run_quiz()
