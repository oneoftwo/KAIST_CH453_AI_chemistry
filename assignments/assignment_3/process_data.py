from rdkit import Chem 
import os 
import pickle 


def read_xyz_to_mol(fn):
    sdf_fn = f"{fn[:-4]}.sdf"
    os.system(f"obabel {fn} -O {fn[:-4]}.sdf")
    mol = Chem.SDMolSupplier(sdf_fn)[0] 
    return mol


fn = "./data/dsgdb9nsd_000001.xyz"
read_xyz_to_mol(fn)


mol_list = []
gap_list = []
for i in range(1, 1001):
    if len(str(i)) == 1:
        fn = f"./data/dsgdb9nsd_00000{i}.xyz"
    elif len(str(i)) == 2:
        fn = f"./data/dsgdb9nsd_0000{i}.xyz"
    elif len(str(i)) == 3:
        fn = f"./data/dsgdb9nsd_000{i}.xyz"
    elif len(str(i)) == 4:
        fn = f"./data/dsgdb9nsd_00{i}.xyz"
    else:
        fn = None
    
    f = open(fn, "r")
    line = f.readlines()[1].strip().split()[9]
    line = str(line)          
    mol = read_xyz_to_mol(fn)
    if mol is None:
        continue
    mol.SetProp("gap", line)
    mol_list.append(mol)
    gap_list.append(float(line))
    print(mol.GetProp("gap"))
    
save_fn = f"./mol.pkl"
pickle.dump(mol_list, open(save_fn, "wb"))
save_fn = f"./gap.pkl"
pickle.dump(gap_list, open(save_fn, "wb"))

    
