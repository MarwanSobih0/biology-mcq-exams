import streamlit as st
import random
import time

# Handle rerun compatibility
if hasattr(st, 'rerun'):
    rerun_func = st.rerun
else:
    rerun_func = st.experimental_rerun

st.set_page_config(page_title="Biology MCQ Exams", page_icon="📚", layout="wide")

# Strong White + Clear Professional Style
st.markdown("""
    <style>
    * {
        box-sizing: border-box;
    }
    .main, .stApp, body {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }
    h1 {
        color: #1D4ED8 !important;
        font-weight: 800 !important;
        text-align: center !important;
        letter-spacing: 0.02em;
        margin: 28px 0 14px 0;
    }
    .stMarkdown h3 {
        color: #1E3A8A !important;
        font-weight: 700 !important;
        margin-top: 10px;
    }
    .stMarkdown p, .stMarkdown li, .stRadio label, .stSelectbox label {
        color: #0F172A !important;
        font-size: 1.05rem !important;
        font-weight: 500 !important;
    }
    .stRadio, .stSelectbox {
        margin-bottom: 16px !important;
    }
    .stRadio > div {
        background-color: #F0F7FF !important;
        padding: 25px !important;
        border-radius: 15px !important;
        border: 3px solid #BFDBFE !important;
        margin-bottom: 20px;
    }
    .stRadio label,
    .stRadio label span,
    div[role='radiogroup'] label,
    div[role='radiogroup'] span,
    div[role='radiogroup'] div {
        font-size: 1.25rem !important;
        color: #1F2937 !important;
        opacity: 1 !important;
        font-weight: 500 !important;
        padding: 12px 0 !important;
        display: block;
    }
    div[role='radiogroup'] *,
    .stRadio label *,
    .stRadio input[type='radio'] {
        color: #1F2937 !important;
        opacity: 1 !important;
        filter: none !important;
    }
    .stSelectbox, .stRadio input[type="radio"] {
        accent-color: #1D4ED8 !important;
    }
    .stButton > button {
        background-color: #2563EB;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 16px 40px;
        font-size: 1.15rem;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #1D4ED8;
    }
    .stSuccess, .stError {
        color: #065F46 !important; /* Dark green for success */
    }
    .stError {
        color: #DC2626 !important; /* Dark red for error */
    }
    .stProgress > div > div > div {
        background-color: #2563EB !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Biology MCQ Exams")
st.markdown("### Professional Academic Assessment Platform")

# ====================== ALL QUESTIONS (COMPLETE) ======================
assignments = {
    "Lecture 1 Assignment": [
        {"q": "1. Which of the following is always necessary when following the scientific method?", 
         "options": ["A) Keep the conditions constant for the experimental variable.", "B) Make sure the hypothesis is testable.", "C) Be as subjective as possible.", "D) All of the above are necessary"], 
         "answer": "B"},
        {"q": "2. The scientific name of the common Pacific seastar is Pisaster ochraceus; it is most closely related to _____.", 
         "options": ["A) Solaster dawsoni, the morning sun star", "B) Pisaster brevispinus, the pink seastar", "C) Leptasterias ochraceus, the six-rayed star", "D) Henricia leviuscula, the blood star"], 
         "answer": "B"},
        {"q": "3. Keeping the internal environment within a tolerable range is called _____.", 
         "options": ["A) hemostasis", "B) homeostasis", "C) balance", "D) response"], 
         "answer": "B"},
        {"q": "4. The level of structure that includes cells of similar structure and function is a/an", 
         "options": ["A) organ system.", "B) tissue.", "C) organ.", "D) species."], 
         "answer": "B"},
        {"q": "5. All the responses of an organism, taken together, constitute the ------------ of the organism.", 
         "options": ["A) homeostasis", "B) metabolism", "C) energy", "D) behavior"], 
         "answer": "D"},
        {"q": "6. The processes by which cells maintain stability are collectively called metabolism.", 
         "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "7. All the individuals of a particular species living in a particular area are called a population.", 
         "options": ["A) True.", "B) False."], "answer": "A"},
        {"q": "8. Which of the following taxonomic classification categories would contain the fewest types of organisms?", 
         "options": ["A) kingdom", "B) family", "C) order", "D) class"], "answer": "B"},
        {"q": "9. Which of the following is not true regarding organisms in the domain Archaea?", 
         "options": ["A) They live in environmental conditions that are too extreme for other organisms.", 
                     "B) They are believed to be the first types of cells to evolve.", 
                     "C) The organisms exist in aquatic environments.", 
                     "D) Most are unicellular, but many are multicellular."], "answer": "D"},
        {"q": "10. The first word in a scientific name (e.g., Panthera leo) is the", 
         "options": ["A) phylum.", "B) species.", "C) genus.", "D) family."], "answer": "C"},
        {"q": "11. After developing a hypothesis, the next step when following the scientific method is to formulate a scientific theory.", 
         "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "12. The eye of the parrotfish is considered an organ because _____.", 
         "options": ["a. the eye of a parrotfish is a multicellular structure", 
                     "b. it is constructed from cells", 
                     "c. the eye is a living structure", 
                     "d. eyes are constructed from several types of tissues interacting together"], "answer": "d"},
        {"q": "13. Science can, or can attempt to, answer all of the following questions except _____.", 
         "options": ["a. why the parrotfish is green", "b. how the cheetah became such a swift predator", 
                     "c. the purpose for human life", "d. how the carbon atom is constructed"], "answer": "c"}
    ],

    "Assignment 2": [
        {"q": "Q1. The main purpose of biological classification is to:", "options": ["A. Name organisms using Latin", "B. Arrange organisms by size", "C. Organize biodiversity and reflect evolutionary relationships", "D. Identify only harmful organisms"], "answer": "C"},
        {"q": "Q2. Which of the following represents the correct order of taxonomic categories from highest to lowest?", "options": ["A. Kingdom → Domain → Phylum → Species", "B. Domain → Kingdom → Phylum → Class", "C. Domain → Phylum → Kingdom → Species", "D. Kingdom → Phylum → Domain → Species"], "answer": "B"},
        {"q": "Q3. Which taxonomic rank contains organisms that are most closely related?", "options": ["A. Family", "B. Order", "C. Genus", "D. Species"], "answer": "D"},
        {"q": "Q4. Binomial nomenclature consists of:", "options": ["A. Kingdom and species names", "B. Genus and species names", "C. Family and genus names", "D. Domain and kingdom names"], "answer": "B"},
        {"q": "Q5. Which of the following is written correctly according to binomial nomenclature rules?", "options": ["A. homo Sapiens", "B. Homo Sapiens", "C. Homo sapiens", "D. homo sapiens"], "answer": "C"},
        {"q": "Q6. Which of the following organisms belongs to the domain Archaea?", "options": ["A. Escherichia coli", "B. Amoeba", "C. Halophiles", "D. Mushroom"], "answer": "C"},
        {"q": "Q7. A major difference between prokaryotic and eukaryotic cells is:", "options": ["A. Presence of ribosomes", "B. Presence of a nucleus", "C. Presence of DNA", "D. Presence of a cell membrane"], "answer": "B"},
        {"q": "Q8. Which group is considered the most diverse and least natural group of eukaryotes?", "options": ["A. Plants", "B. Animals", "C. Fungi", "D. Protists"], "answer": "D"},
        {"q": "Q9. Which characteristic is common to all fungi?", "options": ["A. Photosynthesis", "B. Cell wall made of cellulose", "C. Heterotrophic nutrition by absorption", "D. Presence of chloroplasts"], "answer": "C"},
        {"q": "Q10. Humans belong to which phylum?", "options": ["A. Arthropoda", "B. Mollusca", "C. Chordata", "D. Annelida"], "answer": "C"}
    ],

    "Assignment 3": [
        {"q": "1. In a hydrolysis reaction", "options": ["A) water is removed as the reaction proceeds.", "B) water is used to break a covalent bond.", "C) water molecules are used to dissolve organic molecules.", "D) polymers are synthesized."], "answer": "B"},
        {"q": "2. All of the following is true about sucrose EXCEPT", "options": ["A) it is formed of glucose and fructose", "B) it is a hydrophilic disaccharide", "C) it is formed of two monomers of glucose", "D) it is sometimes called sugarcane"], "answer": "C"},
        {"q": "3. Of the following, which is true for all lipids?", "options": ["A) They are hydrophobic.", "B) They are unsaturated.", "C) They are solid at room temperature.", "D) Found exclusively in animals."], "answer": "A"},
        {"q": "4. Which of the following is NOT a function of proteins in living things?", "options": ["A) formation of the sex hormones", "B) transport of oxygen", "C) binding to disease-causing bacteria", "D) make up hair and fur"], "answer": "A"},
        {"q": "5. The sequence of amino acids in a protein is called the", "options": ["A) secondary structure.", "B) globular form.", "C) primary structure.", "D) peptide bond"], "answer": "C"},
        {"q": "6. In order for a molecule to be classified as 'organic,' it must be found in an organism.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "7. Which of the following is not true of carbon?", "options": ["A) It can bond with four different elements.", "B) It forms a negative ion when in solution.", "C) It can form long chains.", "D) It participates in covalent bonding."], "answer": "B"},
        {"q": "8. All hydrocarbons are insoluble in water.", "options": ["A) True.", "B) False."], "answer": "A"},
        {"q": "9. Cellulose", "options": ["A) is an energy source for humans.", "B) is the most abundant organic molecule on Earth.", "C) has the same chemical structure as starch.", "D) is a major component in the exoskeleton of crustaceans and insects."], "answer": "B"},
        {"q": "10. Unsaturated fatty acids are liquid at room temperature because the hydrocarbon chains are shorter than in saturated fatty acids.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "11. Of the following, which is not a lipid?", "options": ["A) cholesterol", "B) phospholipid", "C) chitin", "D) oil"], "answer": "C"},
        {"q": "12. The joining of two adjacent amino acids is by a/an", "options": ["A) hydrolysis reaction.", "B) ionic bond.", "C) peptide bond.", "D) carboxyl group."], "answer": "C"},
        {"q": "13. DNA and RNA both contain the five-carbon carbohydrate ribose.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "14. In a DNA molecule, cytosine is always paired with", "options": ["A) adenine.", "B) cytosine.", "C) guanine.", "D) uracil."], "answer": "C"},
        {"q": "15. Observations of denatured protein support which conclusion?", "options": ["a. a protein's structure dictates it function", "b. proteins are intolerant of any disruption at any structural level", "c. once the denaturing event ends, the protein will reassume a functional status", "d. all diseases can ultimately be associated with protein denaturation"], "answer": "a"},
        {"q": "16. Low-density lipoprotein (LDL) is referred to as 'bad' cholesterol because the cholesterol", "options": ["A) is chemically altered so as to be indigestible.", "B) is being carried from the cells to the liver.", "C) binds to red blood cells and impairs the transport of oxygen.", "D) is being carried from the liver to the cells."], "answer": "D"},
        {"q": "17. Which of the following is true regarding amino acids and proteins?", "options": ["A) only 9 amino acids are essential", "B) The human body can make all 20 amino acids.", "C) Nutritionists recommend that protein should supply 40-50% of the dietary calories.", "D) All the above are true."], "answer": "A"},
        {"q": "18. Which of the following shows the correct order of oils, ranked from the healthiest to the least healthy?", "options": ["A) Olive oil> canola oil> sunflower oil> corn oil", "B) Corn oil> canola oil> sunflower oil> olive oil", "C) Olive oil> corn oil> sunflower oil> canola oil", "D) Corn oil> sunflower oil> olive oil> canola oil"], "answer": "A"}
    ],

    "Assignment 4": [
        {"q": "1. The pathway for a protein destined for incorporation into the plasma membrane would be _____.", "options": ["A) lysosome -> rough ER -> plasma membrane", "B) nuclear ribosome -> nuclear pore -> plasma membrane", "C) rough ER -> Golgi body -> plasma membrane", "D) rough ER -> ribosome-> plasma membrane"], "answer": "C"},
        {"q": "2. Which of the following statements about nuclear envelope is NOT true", "options": ["A) the structure of nuclear membrane is different from that of cell membrane", "B) in fact it is formed of two membranes", "C) it has pores", "D) it regulates movement of materials to nucleus"], "answer": "A"},
        {"q": "3. Which of the following is an incorrect match?", "options": ["A) lysosome--cell death.", "B) nucleus--surrounded by a double membrane.", "C) smooth endoplasmic reticulum--ATP production.", "D) Golgi apparatus--lipid modification.", "E) rough endoplasmic reticulum – protein synthesis"], "answer": "C"},
        {"q": "4. The structural and functional units of the body are", "options": ["A) cells", "B) tissues", "C) organs", "D) organ systems"], "answer": "A"},
        {"q": "5. The major difference between a prokaryotic cell and a eukaryotic cell is that prokaryotic cells have a cell wall, and eukaryotic cells never have a cell wall.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "6. Which of the following is not true regarding the plasma membrane?", "options": ["A) It is selective as to what enters and exits the cell.", "B) It is a liquid at body temperature.", "C) It has proteins embedded in it.", "D) It separates the nucleus from the cytoplasm."], "answer": "D"},
        {"q": "7. The nucleolus is a region in eukaryotic DNA where ribosomal RNA (rRNA) is produced and where rRNA joins with proteins.", "options": ["A) True.", "B) False."], "answer": "A"},
        {"q": "8. The ______________ is/are the organelle where proteins are synthesized.", "options": ["A) nucleus", "B) ribosomes", "C) lysosomes", "D) endoplasmic reticulum"], "answer": "B"},
        {"q": "9. Which of the following is an incorrect match?", "options": ["A) mitochondrion--oxygen consumption", "B) nucleus--surrounded by a double membrane.", "C) smooth endoplasmic reticulum--ATP production.", "D) Golgi apparatus--lipid modification."], "answer": "C"},
        {"q": "10. The primary function of vacuoles in a cell is for the processing of proteins.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "11. Lysomes function in", "options": ["A) removal of excess water from the cell.", "B) intracellular digestion.", "C) lipid packaging.", "D) membrane transport processes."], "answer": "B"},
        {"q": "12. Which of these processes does not use ATP?", "options": ["A) muscle contraction", "B) membrant transport", "C) protein synthesis", "D) All these processes use ATP."], "answer": "D"},
        {"q": "13. Which of the following is not true for mitochondria?", "options": ["A) They contain many enzymes.", "B) They contain DNA.", "C) They are the site of ATP synthesis in the cell.", "D) They are bound by a single membrane."], "answer": "D"},
        {"q": "14. Microtubules are the cellular structures that allow for movement of the organelles within the cell.", "options": ["A) True.", "B) False."], "answer": "A"},
        {"q": "15. In many types of tissues, a/an _______________ holds the individual cells together in a flexible, sturdy sheet.", "options": ["A) tight junction", "B) plasmodesmata", "C) adhesion junction", "D) gap junction"], "answer": "C"},
        {"q": "16. Which of the following is not true regarding ATP?", "options": ["A) It contains more energy after its terminal phosphate group has been removed.", "B) Most of it is made in the mitochondria of the cells.", "C) A sugar is part of its chemical structure.", "D) It is used in the transporting of chemicals across the plasma membrane."], "answer": "A"},
        {"q": "17. The _____________ is/are responsible for cell shape and the movement of cellular components.", "options": ["A) flagella.", "B) microtubules", "C) lysosomes.", "D) ribosomes."], "answer": "B"},
        {"q": "18. Which is not true about microtublues", "options": ["a. Polar and dynamic", "b. involved in cell division", "c. formed of actin", "d. arise from MTOCs"], "answer": "c"},
        {"q": "19. All of the following is true about cell theory except:", "options": ["A) organisms consist of one or more cells", "B) life continuity arise directly from big cells", "C) cell is the smallest unit that displays the properties of life"], "answer": "B"},
        {"q": "20. Which type of membrane protein determines which cell will respond to a specific hormone or signal?", "options": ["A) Enzymatic proteins", "B) Channel proteins", "C) Receptor proteins", "D) Recognition proteins"], "answer": "C"},
        {"q": "21. Aquaporins in kidney cells are examples of which type of membrane protein?", "options": ["A) Channel proteins", "B) Receptor proteins", "C) Junction proteins", "D) Enzymatic proteins"], "answer": "A"},
        {"q": "22. The proteins that hold cells of the same type together, such as in the urinary bladder, are called:", "options": ["A) Transport proteins", "B) Junction proteins", "C) Recognition proteins", "D) Receptor proteins"], "answer": "B"},
        {"q": "23. Which membrane proteins help the immune system distinguish “self” from “non-self”?", "options": ["A) Enzymatic proteins", "B) Recognition proteins (glycoproteins)", "C) Transport proteins", "D) Junction proteins"], "answer": "B"},
        {"q": "24. Which type of protein is attached to the membrane and catalyzes reactions essential for cell function?", "options": ["A) Enzymatic proteins", "B) Receptor proteins", "C) Channel proteins", "D) Recognition proteins"], "answer": "A"},
        {"q": "25. The Na⁺–K⁺ pump is an example of which type of protein?", "options": ["A) Junction proteins", "B) Receptor proteins", "C) Transport proteins", "D) Recognition proteins"], "answer": "C"},
        {"q": "26. Lysosomes are formed by budding from which organelle?", "options": ["A) Endoplasmic reticulum", "B) Golgi bodies", "C) Nucleus", "D) Plasma membrane"], "answer": "B"},
        {"q": "27. What type of enzymes do lysosomes contain?", "options": ["A) Oxidative enzymes", "B) Hydrolytic enzymes", "C) Glycolytic enzymes", "D) Photosynthetic enzymes"], "answer": "B"},
        {"q": "28. When do lysosomal enzymes become activated?", "options": ["A) When exposed to cytoplasm", "B) After fusion with another vesicle", "C) When transported out of the cell", "D) During protein synthesis"], "answer": "B"},
        {"q": "29. Which of the following best describes the function of lysosomes?", "options": ["A) Protein synthesis", "B) Cellular respiration", "C) Cellular digestion and programmed cell death", "D) Photosynthesis"], "answer": "C"},
        {"q": "30. Tay-Sachs disease is caused by:", "options": ["A) Lysosomes producing too many enzymes", "B) Lysosomes missing enzymes needed to break down lipids", "C) Overactive mitochondria", "D) Excessive ribosome activity"], "answer": "B"},
        {"q": "31. Which cytoskeletal element is the thinnest and most dynamic?", "options": ["A) Microtubules", "B) Intermediate filaments", "C) Actin filaments", "D) Centrioles"], "answer": "C"},
        {"q": "32. Actin filaments are composed of:", "options": ["A) Tubulin dimers", "B) Actin protein chains", "C) Keratin proteins", "D) Microtubule triplets"], "answer": "B"},
        {"q": "33. Which of the following is NOT a function of actin filaments?", "options": ["A) Muscle contraction", "B) Maintenance of cell shape", "C) Intracellular digestion", "D) Cell movement"], "answer": "C"},
        {"q": "34. The structure of a centriole is described as:", "options": ["A) 9 × 2 + 2 arrangement", "B) 9 × 3 + 0 arrangement", "C) 9 × 2 + 0 arrangement", "D) 9 × 3 + 2 arrangement"], "answer": "B"},
        {"q": "35. A centrosome consists of:", "options": ["A) One centriole only", "B) Two centrioles arranged perpendicular to each other", "C) Two centrioles parallel to each other", "D) Four centrioles in a square"], "answer": "B"},
        {"q": "36. The spindle fibers formed by centrioles are important for:", "options": ["A) DNA replication", "B) Attaching to chromosomes during cell division", "C) Protein synthesis", "D) Cytoplasmic streaming"], "answer": "B"},
        {"q": "37. Tight junctions serve to:", "options": ["A) Provide flexible support against stretching", "B) Prevent leakage of water-soluble substances between cells", "C) Allow direct exchange of ions between cells", "D) Anchor cells to the extracellular matrix"], "answer": "B"},
        {"q": "38. Which statement about tight junctions in the stomach is correct?", "options": ["A) They allow HCl to pass freely", "B) They prevent HCl from leaking between gastric cells", "C) They only exist in plant cells", "D) They function as adhesion junctions"], "answer": "B"},
        {"q": "39. Adhesion junctions are especially important in organs subjected to:", "options": ["A) Photosynthesis", "B) Stretch and mechanical stress (stomach, bladder, heart)", "C) Neuronal signaling", "D) Digestion of macromolecules"], "answer": "B"},
        {"q": "40. Gap junctions allow:", "options": ["A) Cells to stretch and remain flexible", "B) Direct and rapid flow of substances between identical cells", "C) Tight sealing between cells", "D) Only protein synthesis between cells"], "answer": "B"}
    ],

    "Assignment 5": [
        {"q": "1. Enzymes", "options": ["A) are usually composed of lipid combined with protein.", "B) must always have at least two substrates to be active.", "C) accelerate chemical reactions.", "D) generally work by raising the energy of activation for a cellular reaction."], "answer": "C"},
        {"q": "2. When a cell is placed in a hypotonic solution,", "options": ["A) water leaves the cell.", "B) no movement of water occurs, but solute moves across the plasma membrane.", "C) water and solute enter the cell.", "D) water diffuses into cell."], "answer": "D"},
        {"q": "3. Facilitated diffusion differs from simple diffusion in that facilitated diffusion", "options": ["A) requires ATP.", "B) requires proteins.", "C) involves nonpolar substances.", "D) moves substances from high to low concentration."], "answer": "B"},
        {"q": "4. Active transport is the cellular process used to establish equal concentrations of ions on both sides of the plasma membrane.", "options": ["A) True", "B) False."], "answer": "B"},
        {"q": "5. The sodium-potassium pump", "options": ["A) is present in the cytosol of the cell.", "B) is a passive process.", "C) helps establish an electrochemical gradient across the membrane.", "D) moves sodium and potassium down their concentration gradients."], "answer": "C"},
        {"q": "6. The process by which vesicles are used to transport digestive enzymes and hormones out of the cell is called", "options": ["A) exocytosis.", "B) exclusion.", "C) pinocytosis.", "D) endocytosis."], "answer": "A"},
        {"q": "7. The process by which substances are brought into the cell by specific receptors is called", "options": ["A) receptor migration", "B) cytointernalization.", "C) receptor-mediated endocytosis.", "D) phagocytosis."], "answer": "C"},
        {"q": "8. Feedback inhibition is a cellular process in which two substrates compete for the active site of an enzyme.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "9. The process by which vesicles release their contents to the outside of the cell only when the cell is stimulated by a signal is called regulated secretion.", "options": ["A) True", "B) False."], "answer": "A"},
        {"q": "10. Which of the following is NOT true regarding the complete breakdown of glucose?", "options": ["A) Water is an end product of the reactions.", "B) ATP is produced.", "C) Glucose breakdown occurs in all cells of the body.", "D) The reactions take place exclusively in the mitochondria."], "answer": "D"},
        {"q": "11. The preparatory (prep) reaction occurs in the space between the outer and inner mitochondrial membranes.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "12. The end product of glycolysis is", "options": ["A) glucose.", "B) pyruvate.", "C) water.", "D) citric acid."], "answer": "B"},
        {"q": "13. Nonprotein substances that assist enzymes are called", "options": ["A) coenzymes.", "B) substrates.", "C) cofactors.", "D) activators."], "answer": "C"},
        {"q": "14. Which of the following is true regarding glycolysis?", "options": ["A) NADH is consumed during the reactions.", "B) The reactions take place in the mitochondria.", "C) Glycolysis results in a net gain of 2 ATP.", "D) Glucose is broken down into 2 molecules of acetyl-coenzyme A."], "answer": "C"},
        {"q": "15. The electron transport chain is a series of electron carriers in the cristae of the mitochondria.", "options": ["A) True.", "B) False."], "answer": "A"},
        {"q": "16. In the complete breakdown of a glucose molecule, 3 NADH molecules are produced which donate electrons to the electron transport chain.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "17. The oxygen consumed by the reactions of cellular respiration becomes part of what molecule?", "options": ["A) ATP.", "B) CO₂.", "C) water.", "D) pyruvate."], "answer": "C"},
        {"q": "18. As the electrons from one FADH₂ molecule are passed through the electron transport chain, 3 ATP are produced.", "options": ["A) True.", "B) False."], "answer": "B"},
        {"q": "19. Most of the ATP produced from the breakdown of glucose comes from", "options": ["A) the electron transport chain.", "B) the citric acid cycle.", "C) glycolysis.", "D) substrate-level phosphorylation."], "answer": "A"},
        {"q": "20. Which of the following is true of fermentation?", "options": ["A) It occurs in the mitochondria.", "B) It gives a net gain of four ATP.", "C) It occurs in times of glucose deprivation.", "D) It begins with glucose."], "answer": "D"},
        {"q": "21. Which of the following is NOT a possible product of fermentation?", "options": ["A) alcohol.", "B) NADH.", "C) lactic acid."], "answer": "B"},
        {"q": "22. The preparatory (prep) reaction occurs in the mitochondrial matrix.", "options": ["A) True.", "B) False."], "answer": "A"},
        {"q": "23. Glucose crosses the cell membrane, while galactose, a very similar molecule, cannot. How can this be explained?", "options": ["a. membrane transporter is specific for glucose – galactose can't enter the transporter", "b. glucose is larger than galactose, so the receptor proteins bind glucose more effectively", "c. glucose gets through but galactose is blocked by osmosis"], "answer": "a"},
        {"q": "24. Which observation(s) would distinguish an active transport system from a passive system?", "options": ["a. transport rate was sensitive to temperature and pH", "b. transport rate declined when an inhibitor was used to prevent the hydrolysis of ATP", "c. transport rate is not dependent on the concentration gradient", "d. all of the choices would characterize active transport"], "answer": "d"},
        {"q": "25. Meals with a high salt content can temporarily cause blood plasma to become _____, and red blood cells to _____.", "options": ["a. hypotonic, shrink", "b. hypertonic, swell", "c. hypotonic, swell", "d. hypertonic, shrink"], "answer": "d"},
        {"q": "26. Why does a drop of food coloring diffuse more rapidly in warm water than in cold?", "options": ["a. collisions with rapidly moving water molecules disperse the food coloring more quickly", "b. warm food coloring expands, becomes less dense, and floats toward the surface", "c. temperature differences increase the steepness of the concentration gradient"], "answer": "a"},
        {"q": "27. Which of the following do enzymes and membrane carriers have in common?", "options": ["a. they recognize molecules by shape", "b. they are constructed from protein", "c. both choices are true"], "answer": "c"},
        {"q": "28. Which of the following would diffuse most easily across a cell membrane?", "options": ["a. carbon dioxide", "b. glucose", "c. glycogen"], "answer": "a"},
        {"q": "29. What cofactor accepts electrons in both glycolysis and the Krebs cycle?", "options": ["a. ATP", "b. NADP", "c. FAD", "d. NAD", "e. CoA"], "answer": "d"},
        {"q": "30. Prior to entering the Krebs cycle, pyruvate loses _____ and is converted to _____.", "options": ["a. a water, acetyl-CoA", "b. a carbon dioxide, oxaloacetate", "c. a carbon dioxide, acetyl-CoA", "d. a water, oxaloacetate", "e. electrons, lactate"], "answer": "c"},
        {"q": "31. The oxidation of citrate to a 5-carbon intermediate is coupled with the reduction of _____ to _____.", "options": ["a. FADH₂, FAD", "b. FAD, FADH₂", "c. NADH, NAD⁺", "d. NAD⁺, NADH"], "answer": "d"},
        {"q": "32. The energy released during electron transfer reactions is initially used to push _____ into the outer compartment.", "options": ["a. electrons", "b. NADH", "c. hydrogen ions", "d. oxygen"], "answer": "c"},
        {"q": "33. What is the typical yield of ATP from the complete aerobic respiration of glucose?", "options": ["a. 36", "b. 24", "c. 12", "d. 6", "e. 4"], "answer": "a"},
        {"q": "34. When muscle cells are deprived of oxygen, they can continue to form ATP through ____.", "options": ["a. lactate fermentation", "b. alcoholic fermentation", "c. anaerobic electron transfer", "d. sulfur reduction"], "answer": "a"},
        {"q": "35. In human cells, the pyruvate formed at the end of glycolysis can be converted to _____.", "options": ["a. ethanol or lactate", "b. lactate or acetyl CoA", "c. ethanol, lactate, or acetyl CoA", "d. ethanol or acetyl CoA"], "answer": "b"},
        {"q": "36. How many ATP molecules are formed during the Krebs cycle for each acetyl-CoA that enters?", "options": ["a. 0", "b. 1", "c. 2", "d. 4", "e. 6"], "answer": "b"},
        {"q": "37. Where in the mitochondrion are the electron transfer chains located?", "options": ["a. in the inner compartment", "b. embedded in the inner membrane", "c. in the outer compartment", "d. embedded in the outer membrane"], "answer": "b"},
        {"q": "38. Which process below is correctly matched with its cellular location?", "options": ["a. glycolysis - mitochondrion", "b. Krebs cycle - cytoplasm", "c. lactic acid fermentation - cytoplasm", "d. electron transfer phosphorylation - Golgi"], "answer": "c"},
        {"q": "39. What is the role of the molecular oxygen (O₂) in aerobic respiration?", "options": ["a. it donates H's and electrons", "b. oxygen combines with carbon from glucose to form CO₂", "c. it transfers H's from the Krebs cycle by temporarily forming water", "d. oxygen accepts electrons from the electron transfer chain and hydrogen ion to form water"], "answer": "d"},
        {"q": "40. Careful measurement reveals that the cofactors coenzyme A, NAD⁺, and FAD are present in cells in relatively low concentrations. This is not surprising because _____.", "options": ["a. each becomes toxic at higher concentrations and would damage cell metabolism", "b. like enzymes, each can be used over and over", "c. they are costly molecules to synthesize and cells make them only as needed", "d. each is degraded immediately after being used, preventing any buildup from occurring", "e. their roles in aerobic respiration are extremely minor"], "answer": "b"}
    ]
}

# ====================== APP LOGIC ======================
selected_exam = st.sidebar.selectbox("Select Assignment", list(assignments.keys()))

# Keep the shuffled question list stable across reruns
if 'questions' not in st.session_state or st.session_state.get('last_exam') != selected_exam:
    st.session_state.questions = assignments[selected_exam].copy()
    random.shuffle(st.session_state.questions)
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = [False] * len(st.session_state.questions)
    st.session_state.last_exam = selected_exam

questions = st.session_state.questions
current = st.session_state.current
q = questions[current]

st.subheader(f"Question {current + 1} of {len(questions)}")
st.markdown(f"**{q['q']}**")

selected = st.radio("Choose the correct answer:", q["options"], key=f"q_{current}")

feedback_placeholder = st.empty()

if st.button("Submit Answer", type="primary", use_container_width=True):
    if not st.session_state.answered[current]:
        user_choice = selected.strip()[0].upper() if selected else ""
        correct = q["answer"].strip().upper()

        st.session_state.answered[current] = True

        if user_choice == correct:
            feedback_placeholder.success("✅ Correct Answer! Well done.")
            st.session_state.score += 1
        else:
            feedback_placeholder.error(f"❌ Wrong! The correct answer is **{correct}**")

        time.sleep(1.6)
        feedback_placeholder.empty()
        if current < len(questions) - 1:
            st.session_state.current += 1
            rerun_func()
        else:
            percentage = (st.session_state.score / len(questions)) * 100
            st.balloons()
            st.success(f"""
            🎉 **Exam Completed!**

            **Your Score:** {st.session_state.score} / {len(questions)}  
            **Percentage:** {percentage:.1f}%

            {'🌟 Outstanding Performance!' if percentage >= 85 else 
             '👍 Very Good!' if percentage >= 70 else 
             '✅ You Passed!' if percentage >= 50 else '📚 Keep Studying Harder!'}
            """)

st.progress((current + 1) / len(questions))
st.caption(f"**Current Score:** {st.session_state.score} / {len(questions)}")

if st.button("🔄 Restart This Exam", use_container_width=True):
    for key in list(st.session_state.keys()):
        if key != "last_exam":
            del st.session_state[key]
    rerun_func()
