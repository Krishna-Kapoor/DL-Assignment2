"""
MAI/IDL SS26 - Final assignment. 

MG 6/6/2026
"""
import torch
from pathlib import Path
from torch.utils.data import TensorDataset, DataLoader

# Initially incorrect data path, now updated it resolve bugs-----Bug1
def get_loaders(data, data_path, batch_size, val_split=0.1):
    d_path = Path(data_path) / f"{data}.pt"
    data_dict = torch.load(d_path)

    total_samples = data_dict['train_images'].shape[0]
    val_size = int(total_samples * val_split)   # Split the training dataset into training and validation dataset----Bug2
    val_start = total_samples - val_size
    train_data = data_dict['train_images'][:val_start]
  # Added squeeze to return 0d or 1 d tensor which resolves runtime errors----Bug3
    train_labels = torch.squeeze(data_dict['train_labels']) [:val_start]
    val_data = data_dict['train_images'][val_start:]
    val_labels =torch.squeeze(data_dict['train_labels'])[val_start:]
    #Added squeeze to return 0d or 1d tensor which resolves runtime errors
    test_labels = torch.squeeze(data_dict['test_labels'])

  # added normalization to datasets----Bug4
    mean = train_data.mean(dim=(0,2,3), keepdim=True)
    std = train_data.std(dim=(0,2,3), keepdim=True) + 1e-8  # Added small value to avoid division by zero
    train_data = (train_data - mean) / std
    val_data = (val_data - mean) / std
    test_data = (data_dict['test_images'] - mean) / std

    train_dataset = TensorDataset(train_data, train_labels)
    val_dataset = TensorDataset(val_data, val_labels)
    test_dataset = TensorDataset(test_data, test_labels)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(dataset=val_dataset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, val_loader, test_loader