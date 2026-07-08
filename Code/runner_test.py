"""
MAI/IDL SS26 - Final assignment.
Runner script to train and evaluate all models across all datasets.
"""
"""This file runs the """

import sys
import time
from pathlib import Path

import torch      #Created runner test file  for running all models on all datasets simultaneously and collecting results 
import torch.nn as nn
import torch.optim as optim

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from data import get_loaders
import models
from fit import Trainer

torch.manual_seed(42)  # For reproducibility

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

DATASET_CONFIG = {
    "cells":   {"CHANNELS": 3, "NUM_CLASSES": 8},
    "chest":   {"CHANNELS": 1, "NUM_CLASSES": 2},
    "lesions": {"CHANNELS": 3, "NUM_CLASSES": 7},
    "orgs":    {"CHANNELS": 1, "NUM_CLASSES": 11},
}

MODEL_SET = ["AlexNet", "VGG16", "ResNet18", "GreenNet"]
 
DATA_PATH = "Data"
BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 15
DROPOUT_RATE = 0.5
ACTIVATION_STR = "ReLU"
WEIGHT_DECAY = 1e-4

results = []

for data in DATASET_CONFIG:
    for model in MODEL_SET:
        torch.cuda.reset_peak_memory_stats()
        print(f"\n=== {model} on {data} ===")
        start = time.time()
        train_loader, val_loader, test_loader = get_loaders(data=data,data_path=DATA_PATH,batch_size=BATCH_SIZE)
        model_class = getattr(models,model)
        model_name = model_class(in_channels=DATASET_CONFIG[data]["CHANNELS"],num_classes=DATASET_CONFIG[data]["NUM_CLASSES"],drop_rate=DROPOUT_RATE,activation_str=ACTIVATION_STR).to(device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model_name.parameters(), lr=LEARNING_RATE, weight_decay=WEIGHT_DECAY)
        trainer = Trainer(model_name, criterion, optimizer, device)
        trainer.fit(train_loader, val_loader, epochs=EPOCHS)
        duration = time.time() - start
        train_memory = torch.cuda.max_memory_allocated() / (1024**2) 
        #torch.cuda.synchronize()  
        #stop_watch = time.time()
        #test_loss, test_acc, test_precision, test_recall, test_f1 = trainer.evaluate(test_loader)
        #torch.cuda.synchronize() 
        #stop_watch = time.time() - stop_watch
        #latency_per_sample = (stop_watch / len(test_loader.dataset)) * 1000
        torch.cuda.synchronize()  
        stop_watch = time.time()
        test_loss, test_acc, test_precision, test_recall, test_f1 = trainer.test(test_loader)
        torch.cuda.synchronize() 
        stop_watch = time.time() - stop_watch
        latency_per_sample = (stop_watch / len(test_loader.dataset)) * 1000
        results.append({
        "model_name": model,
        "dataset": data,
        "test_loss": test_loss,
        "test_acc": test_acc,
        "precision": test_precision,
        "recall": test_recall,
        "f1": test_f1,
        "duration": duration,
        "memory_mb": train_memory,
        "latency_ms": latency_per_sample})

print("\n" + "="*50)
print("FINAL RESULTS SUMMARY")
print("="*50)
for r in results:
    print(f"{r['model_name']} on {r['dataset']} | "
          f"P: {r['precision']:.4f} | "
          f"R: {r['recall']:.4f} | "
          f"Test Loss: {r['test_loss']:.4f} | "
          f"Test Acc: {r['test_acc']:.2f}% | "
          f"F1: {r['f1']:.4f} | "
          f"Time: {r['duration']:.1f}s |"
          f"Memory: {r['memory_mb']:.1f}MB | "
          f"Latency: {r['latency_ms']:.3f}ms/sample")