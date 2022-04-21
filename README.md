# Molecular Learning with Graph Transformers to Predict Blood-Brain-Barrier Penetration 

<!-- badges: start -->

![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)

<!-- badges: end -->

Here, I use [Graphormer](https://www.microsoft.com/en-us/research/project/graphormer/), first published at [NeurIPS 2021](https://openreview.net/forum?id=OeWooOxFwDa), to predict whether molecules from the [Therapeutics Data Commons](https://tdcommons.ai) [Blood-Brain Barrier Dataset](https://tdcommons.ai/single_pred_tasks/adme/#bbb-blood-brain-barrier-martins-et-al) (derived from [Martins et al., 2012](https://doi.org/10.1021/ci300124c)) can penetrate the blood-brain barrier.


## Setup

Based on the [Graphormer Installation Guide](https://graphormer.readthedocs.io/en/latest/Installation-Guide.html), follow the steps below to successfully install and run Graphormer on [O2](https://harvardmed.atlassian.net/wiki/spaces/O2/overview). First, [submit a GPU job on O2](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/1629290761/Using+O2+GPU+resources). For example:

```
srun --pty -t 0-1:00:0 -n 4 --mem=32G -p gpu --gres=gpu:1 /bin/bash
```
Once the resources are provisioned and a `compute` node has been assigned, load the following modules.
```
module load conda2/4.2.13
module load gcc/9.2.0
module load cuda/11.2
```
Next, create a virtual environment.
```
conda create -n graphormer python=3.9
conda activate graphormer
```
Clone the [Graphormer repository](https://github.com/microsoft/Graphormer) and run the installation script.
```
git clone --recursive https://github.com/microsoft/Graphormer.git
cd Graphormer
bash install.sh
```
Important! Uninstall the `setuptools` package; otherwise, the `fairseq` training command will hang at the console without output. See [this issue](https://github.com/microsoft/Graphormer/issues/111).
```
pip uninstall setuptools
```
Finally, navigate to the correct subdirectory to train or evaluate Graphormer. For example:
```
cd examples/property_prediction
bash zinc.sh
```
The absence of `setuptools` may produce a `ModuleNotFoundError` (i.e., `No module named '_distutils_hack'`); however, training should still proceed. Other packages may be needed. Remember, however, to uninstall `setuptools` again should it be re-installed in the installation process for other packages.

First, we must install the [Therapeutics Data Commons](https://tdcommons.ai/start/) package.
```
pip install PyTDC
```
For interactive Jupyter notebooks:
```
pip install jupyterlab
pip install notebook
pip install matplotlib
```
TensorBoard is a visualization toolkit for ML training. TensorBoard logging can be enabled by adding the following flag to the training `.sh` script: `--tensorboard-logdir ./runs \`. To install [TensorBoard](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html):
```
pip install tensorboard
```
To run `tensorboard`, execute the following:
```
tensorboard --logdir=runs
```

## Acknowledgements

This is [Ayush Noori](mailto:anoori@college.harvard.edu)'s final project for [GENED 1125 at Harvard
College](https://gened1125.github.io/spring2022/).


## Selected References

1. Ying, C. et al. Do Transformers Really Perform Badly for Graph Representation? in Advances in Neural Information Processing Systems vol. 34 28877–28888 (Curran Associates, Inc., 2021).

2. Huang, K. et al. Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development. arXiv:2102.09548 [cs, q-bio] (2021).

3. Martins, I. F., Teixeira, A. L., Pinheiro, L. & Falcao, A. O. A Bayesian Approach to in Silico Blood-Brain Barrier Penetration Modeling. J. Chem. Inf. Model. 52, 1686–1697 (2012).

4. Wu, Z. et al. MoleculeNet: a benchmark for molecular machine learning. Chem. Sci. 9, 513–530 (2018).

