"""
MAI/IDL SS26 - Final assignment.
Part 3: Transfer Learning for the orgs dataset.

Strategy:
  - Load a pretrained ResNet18 from torchvision (trained on ImageNet)
  - Freeze all convolutional feature layers
  - Replace the final FC head with one sized for orgs (num_classes)
  - Fine-tune only the new head on orgs training data
  - Compare against scratch training results from runner_test.py
"""
import torch
import torch.nn as nn
import torch.optim as optim
from data import get_loaders
from fit import Trainer
from models import ResNet18
from torchvision.models import resnet18, ResNet18_Weights


class TransferResNet(nn.Module):
    def __init__(self, in_channels=1,num_classes=11):
        super().__init__()
        self.backbone = ResNet18(in_channels=in_channels, num_classes=11)
        for param in self.backbone.parameters():
            param.requires_grad = False

        self.backbone.classifier = nn.Linear(self.backbone.classifier.in_features, num_classes)

    def forward(self, x):

        return self.backbone(x)


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training on device: {device}")

    train_loader, val_loader, test_loader = get_loaders(
        data="organs",
        data_path="Data",
        batch_size=32,
    )

    model = TransferResNet(num_classes=11).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)

    trainer = Trainer(model, criterion, optimizer, device)
    trainer.fit(train_loader, val_loader, epochs=20)
    # Test Evaluation 
    test_loss, test_acc, test_precision, test_recall, test_f1 = trainer.test(test_loader)
    


if __name__ == "__main__":
    main()