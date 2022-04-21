import numpy as np
import torch
from graphormer.data import register_dataset
from tdc.single_pred import ADME
from tdc.chem_utils import MolConvert

@register_dataset("BBB_Martins")
def create_customized_dataset():
    
    # load dataset
    data = ADME(name = 'BBB_Martins')

    # generate data split
    split = data.get_split(method = 'scaffold', seed = 42, frac = [0.7, 0.1, 0.2])

    # append train/test/validation sets, then generate indices
    split_data = split['train'].append(split['valid']).append(split['test'])
    train_idx = np.arange(len(split['train']))
    valid_idx = np.arange(len(split['valid'])) + len(split['train'])
    test_idx = np.arange(len(split['test'])) + len(split['train']) + len(split['valid'])

    # define converter
    converter = MolConvert(src = 'SMILES', dst = 'DGL')

    # construct dataset as list of tuples: (DGL graph, label as tensor)
    dataset = [(converter(x), torch.tensor([y])) for x, y in zip(split_data['Drug'], split_data['Y'])]
    
    # return dataset and train/test/validation indices
    return {
        "dataset": dataset,
        "train_idx": train_idx,
        "valid_idx": valid_idx,
        "test_idx": test_idx,
        "source": "dgl"
    }
