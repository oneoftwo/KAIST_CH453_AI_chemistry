import csv
import os

from PIL import Image
from rdkit import Chem
from rdkit.Chem import Descriptors, Draw

# File path to the SMILES file
smiles_file = "PubChem_30K.txt"

# Directory to save images
output_dir = "images"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
i = 0

smiles_list = []
logp_list = []
tpsa_list = []

with open(smiles_file, "r") as f:
    for line in f:
        _, smiles = line.split(maxsplit=1)
        smiles = smiles.strip()

        if 6 < len(smiles) < 16:
            mol = Chem.MolFromSmiles(smiles)
            img = Draw.MolToImage(mol, size=(96, 96), bgcolor="white")

            img_path = os.path.join(output_dir, f"{i}.png")
            img.save(img_path)

            logP = Descriptors.MolLogP(mol)
            TPSA = Descriptors.TPSA(mol)

            smiles_list.append(smiles)
            logp_list.append(logP)
            tpsa_list.append(TPSA)

            i += 1

# Save the data to a CSV file
output_csv_path = os.path.join(output_dir, "output.csv")
with open(output_csv_path, "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Index", "SMILES", "LogP", "TPSA"])  # Header row
    for idx, (smiles, logP, TPSA) in enumerate(zip(smiles_list, logp_list, tpsa_list)):
        writer.writerow([idx, smiles, logP, TPSA])
