#!/bin/bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh   -b -p  $(pwd)/miniconda3
export PATH="$(pwd)/miniconda3/bin:$PATH"
conda update --yes  -q conda
conda info -a
conda create --yes  --name  testenv python=3.7  scikit-learn
source activate testenv
