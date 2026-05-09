# LABind: Identifying Protein Binding Ligand-Aware Sites via Learning Interactions Between Ligand and Protein

### datasets

`LigBind.7z`, `GPSite.7z`, and `Unseen.7z` represent the three datasets used in `LABind`, corresponding to the DS1, DS2, and DS3 datasets, respectively. Each dataset contains FASTA files, label sequences in binary format (01 sequences), and the corresponding PDB files. After extraction, place datasets in the root directory of `LABind`.  

The file structures for `LigBind.7z` and `GPSite.7z` are as follows:
.
```
LigBind/GPSite
|
├─ fasta
│   ├─ train
│   │   └─ *.fa
│   ├─ test
│   │   └─ *.fa
├─ label
│   ├─ train
│   │   └─ *.fa
│   ├─ test
│   │   └─ *.fa
├─ pdb
│   ├─ train
│   │   └─ *.pdb
│   ├─ test
│   │   └─ *.pdb

```

> ESMFold-predicted and OmegaFold-predicted structures are provided in `DS1_pred_structures.7z`.

The file structure for `Unseen.7z`  is as follows:

```
Unseen
|
├─ fasta
│   ├─ training.fa
│   ├─ picking.fa
│   ├─ test.fa
├─ label
│   ├─ training.fa
│   ├─ picking.fa
│   ├─ test.fa
├─ pdb
│   └─ *.pdb

```

The file structure for `COACH64.7z`  is as follows:

```
COACH64
|
├─ pdb.
│   └─ *.pdb
├─ test.fa
```



### model weights
`model.7z` file contains the weights trained on the three datasets, which can be downloaded and saved in the `./model/` directory within `LABind`. 

The file structure for `model.7z`  is as follows:

```
model
|
├─ LigBind
│   └─ *.ckpt
├─ GPSite
│   └─ *.ckpt
├─ Unseen
│   └─ *.ckpt

```

### ligands

`Ligand.7z` file contains the ligand positions in all test sets. Ligands are named in the format `chain_ligand`. For example, `5qpjA_ZN.pdb` represents the spatial positions of `ZN` ions interacting with chain `A` of the `5qpj` protein.  `Binding_site_centers.7z` contains the spatial centers of ligands.

```
Ligand
|
├─ LigBind
│   └─ *.pdb
├─ GPSite
│   └─ *.pdb
├─ Unseen
│   └─ *.pdb
├─ COACH64
│   └─ *.pdb
│
Binding_site_centers
|
├─ LigBind_binding_site_center.csv
├─ GPSite_binding_site_center.csv
├─ Unseen_binding_site_center.csv
├─ COACH64_binding_site_center.csv
```

