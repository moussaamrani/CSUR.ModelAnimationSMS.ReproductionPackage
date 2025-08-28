# Reproduction Package for the ACM CSUR Systematic Mapping Study (SMS) on Model Animation in MDE

The paper entitled _Animation of Model Transformations in Model-Driven Engineering: A Mapping Study_ is available online at ...  
An author version (preliminary to the official publication, may be missing some information) is available here: ...

---

## Contents of the Reproduction Package

1. **Spreadsheet Listing**  
   Available as a Google Sheet document:  
   - All papers in the CORPUS  
   - Papers selected after the first round but **discarded** due to exclusion criteria  
   - List of TOOLS and their webpages  
   - Some graphs used in the paper  

2. **Corpus Data**  
   - Provided as BibTeX and CSV files  

3. **Python Scripts for Graph Generation**  
   Located in the `python` directory, organized by analysis type:  
   - **Vertical Analysis (`VA`)**: examining each classification dimension individually  
   - **Orthogonal Analysis (`OA`)**: crossing dimensions to generate new insights  

---

## Environment and Dependencies

- Python 3.x  
- Libraries:  
  - `matplotlib` for plotting  
  - `numpy` for numerical operations  
  - `pandas` for data manipulation  
- Platform-independent (tested on Windows, Linux, macOS)  

---

## Usage Instructions

1. Install the required Python libraries:  
```bash
pip install matplotlib numpy pandas
