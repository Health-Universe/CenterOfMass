import streamlit as st
import json
import os
import pandas as pd
import io
import subprocess
import time
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "CenterOfMass"))

from center_of_mass import center_of_mass

st.markdown("## Center of Mass - Protein")
st.divider()

# File uploader
pdb_file = st.file_uploader(
    "Upload",
    type="pdb",
    help="**Input:** Protein PDB \n\n**Output:** Center of Mass of Protein"
)

# File Processing
if pdb_file is not None:
    run_button = st.button("Run", help="Calculating Center of Mass of Protein")
    if run_button:
        with st.spinner("Running..."):
            time.sleep(2)
            # Save files
            pdb_path = "./protein.pdb"
            
            # Read file values
            pdb_data = pdb_file.getvalue()
            
            with open(pdb_path, "wb") as f:
                f.write(pdb_data)
            
            i = "ATOM"
                
            # Run script via subprocess
            command = (
                f"python center_of_mass.py protein.pdb "
                f"-i {i}"
            )
            
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Display the output
            st.divider()
            st.subheader("Output")
            st.write("Center of Mass for the protein is the following:")
            st.code(result.stdout)
            
            

