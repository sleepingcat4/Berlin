# Repository for Sound Wave's Proposal Paper in Beamline for Schools
This repository contains the code for the team Sound Wave's proposal paper in Beamline for Schools. The paper explores the use of classical convolutional neural networks (CNN), quantum CNNs, and hybrid classical-quantum CNNs for analyzing audio spectrograms of particle collision sound waves.

# Notebooks
The notebook folder contains Jupyter notebooks for training and transfer learning of the different models. The train_auto.ipynb notebook demonstrates training a classical CNN using auto differentiation, while **train_tran.ipynb** demonstrates transfer learning on YAMNet. To train a quantum CNN from scratch, the **train_qiskit.ipynb notebook** is used, while **train_penny.ipynb** is used for transfer learning a hybrid classical-quantum CNN (YAMNet).

## Dataset
As creating the dataset is a fundamental aspect of the proposal paper at CERN, we do not provide any pre-attached dataset.

Trained Models
As we do not have an in-built dataset yet for particle collision sound waves, we have not trained any models and cannot provide any pre-trained models at the moment.

Classical vs Hybrid vs Quantum Models
Each model has its own advantages and disadvantages. In most cases, classical models perform better, but quantum-based hybrid models and quantum models tend to show better performance in fewer epochs.

## Conclusion
Our proposal paper at CERN deals with particle collision sound waves and audio spectrograms. These produce faint sounds, and using quantum models to capture these nuances to perform precise experiments and produce concrete results is a natural step forward.

# Copyright
The code is not open sourced, and the copyright belongs to **@sleepingcat4.**
