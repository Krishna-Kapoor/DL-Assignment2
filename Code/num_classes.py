import torch

d = torch.load("Data/organs.pt", weights_only=False)
print("Input channels:", d["train_images"].shape[1])
print("Number of classes:", len(torch.unique(d["train_labels"])))