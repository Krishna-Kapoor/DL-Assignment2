"""
MAI/IDL SS26 - Final assignment. 

MG 6/6/2026
"""
import json

import torch
import torch.nn as nn
import torch.optim as optim
from data import get_loaders
import models
from fit import Trainer

def main():   
    with open("config.json", "r") as f:
        config = json.load(f)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training executing on device: {device}")

    train_loader, val_loader, test_loader = get_loaders(data=config["DATA"], data_path=config["DATA_PATH"], batch_size=config["BATCH_SIZE"])

    model_class = getattr(models, config["MODEL"])
    model = model_class(in_channels=config["CHANNELS"], num_classes=config["NUM_CLASSES"], drop_rate=config["DROPOUT_RATE"], activation_str=config["ACTIVATION_STR"]).to(device)
    criterion = nn.CrossEntropyLoss()    # added drop_out to config file----bug11  and ---activation_str to relu---bug12
    optimizer = optim.Adam(model.parameters(), lr=config["LEARNING_RATE"], weight_decay=config["WEIGHT_DECAY"])

    trainer = Trainer(model, criterion, optimizer, device)
    trainer.fit(train_loader, val_loader, epochs=config["EPOCHS"])
    test_loss, test_acc, test_precision, test_recall, test_f1 = trainer.evaluate(test_loader)
    print(f"\nTest Results | Loss: {test_loss:.4f} - Acc: {test_acc:.2f}% | "
      f"Precision: {test_precision:.4f} - Recall: {test_recall:.4f} - F1: {test_f1:.4f}")

if __name__ == "__main__":
    main()