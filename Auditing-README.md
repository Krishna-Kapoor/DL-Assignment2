MAI-Deep Learning Final Portfolio 2026 
Auditing 
Found out 12 bugs from 4 files: data.py, fit.py, models.py, train.py
-- some bugs were visible from the basic ANN architecture like no torch.zero_grad function , in the absence of which gradients were not getting cleared by defaulte and were getting accumulated.
---Another issue which I found out was that in data.py file, training dataset was not split into training and validation dataset. With validation dataset , it is possible to tune hyperparameters in an optimal manner. 
---Another improvement was that filled activation_str with ReLU instead of Identity.
---Also the path of dataset was corrupted which I found out durng runtime, so this was yet another bug.
---Further, I normalised my datasets before loading through Dtaset and Dataloader class about which I discussed with Shravani and considered it be a good approach.
--- Also , i applied torch.squeeze function to validation labels and train labels since I found out at run time that crossentropy function accepts only 0d or 1d tensor , which was not in current form 
----Also in train.py i changed dropout_rate from 0.99 to 0.50 and changed activation_str from None to relu



-- created file num_classes.py to find out the number of classes and no. of input channels for each dataset--cells,chest,lesions,organs,orgs.pt

---------------------------AlexNet training for cells dataset---------------------------------

After resolving first 10 bugs, I started training with first 5 epochs and got the following results with learning_rate=0.0001:
Training executing on device: cpu

 Starting Training Routine...
--------------------------------------------------
Epoch [01/05] | Train Loss: 0.9384 - Train Acc: 64.01% | Val Loss: 0.4895 - Val Acc: 82.08%
Epoch [02/05] | Train Loss: 0.4355 - Train Acc: 83.44% | Val Loss: 0.3822 - Val Acc: 85.74%
Epoch [03/05] | Train Loss: 0.3203 - Train Acc: 88.21% | Val Loss: 0.2593 - Val Acc: 91.44%
Epoch [04/05] | Train Loss: 0.2510 - Train Acc: 91.22% | Val Loss: 0.5840 - Val Acc: 82.52%
Epoch [05/05] | Train Loss: 0.1973 - Train Acc: 93.16% | Val Loss: 0.2515 - Val Acc: 92.17%
--------------------------------------------------
Training Complete!



Finally Alexnet for cells dataset gave good (crossed baseline accuracy) results for these configurations:"BATCH_SIZE": 32,"LEARNING_RATE": 0.0001,"EPOCHS": 15, "DROPOUT_RATE" : 0.9, "ACTIVATION_STR" : "ReLU" as follows:
Training executing on device: cpu

 Starting Training Routine...
--------------------------------------------------
Epoch [01/15] | Train Loss: 1.7043 - Train Acc: 31.86% | Val Loss: 0.9564 - Val Acc: 61.08%
Epoch [02/15] | Train Loss: 0.8593 - Train Acc: 66.39% | Val Loss: 0.5646 - Val Acc: 76.44%
Epoch [03/15] | Train Loss: 0.6412 - Train Acc: 74.30% | Val Loss: 0.4826 - Val Acc: 79.59%
Epoch [04/15] | Train Loss: 0.5011 - Train Acc: 79.74% | Val Loss: 0.3576 - Val Acc: 85.15%
Epoch [05/15] | Train Loss: 0.3927 - Train Acc: 84.48% | Val Loss: 0.2592 - Val Acc: 91.73%
Epoch [06/15] | Train Loss: 0.3309 - Train Acc: 87.96% | Val Loss: 0.2562 - Val Acc: 90.42%
Epoch [07/15] | Train Loss: 0.2572 - Train Acc: 91.08% | Val Loss: 0.1686 - Val Acc: 94.51%
Epoch [08/15] | Train Loss: 0.2294 - Train Acc: 92.49% | Val Loss: 0.1755 - Val Acc: 94.29%
Epoch [09/15] | Train Loss: 0.2000 - Train Acc: 93.79% | Val Loss: 0.2911 - Val Acc: 89.90%
Epoch [10/15] | Train Loss: 0.1788 - Train Acc: 94.06% | Val Loss: 0.1814 - Val Acc: 94.81%
Epoch [11/15] | Train Loss: 0.1565 - Train Acc: 95.00% | Val Loss: 0.1594 - Val Acc: 95.25%
Epoch [12/15] | Train Loss: 0.1492 - Train Acc: 95.16% | Val Loss: 0.1405 - Val Acc: 95.54%
Epoch [13/15] | Train Loss: 0.1321 - Train Acc: 95.85% | Val Loss: 0.1546 - Val Acc: 95.76%
Epoch [14/15] | Train Loss: 0.1325 - Train Acc: 95.94% | Val Loss: 0.1050 - Val Acc: 96.78%
Epoch [15/15] | Train Loss: 0.1163 - Train Acc: 96.32% | Val Loss: 0.1482 - Val Acc: 95.98%
--------------------------------------------------
Training Complete!

after updating drop_rate=0.5, learning_rate=0.001, epochs=25: got following results:
 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 1.1838 - Train Acc: 54.22% | Val Loss: 0.9721 - Val Acc: 66.64%
Epoch [02/25] | Train Loss: 0.6414 - Train Acc: 76.05% | Val Loss: 0.4117 - Val Acc: 85.08%
Epoch [03/25] | Train Loss: 0.4971 - Train Acc: 82.20% | Val Loss: 0.8412 - Val Acc: 75.64%
Epoch [04/25] | Train Loss: 0.4022 - Train Acc: 85.79% | Val Loss: 0.2957 - Val Acc: 89.10%
Epoch [05/25] | Train Loss: 0.3279 - Train Acc: 88.66% | Val Loss: 0.2916 - Val Acc: 88.30%
Epoch [06/25] | Train Loss: 0.2752 - Train Acc: 90.80% | Val Loss: 0.2489 - Val Acc: 92.32%
Epoch [07/25] | Train Loss: 0.2616 - Train Acc: 91.32% | Val Loss: 0.3081 - Val Acc: 88.15%
Epoch [08/25] | Train Loss: 0.2444 - Train Acc: 91.86% | Val Loss: 0.1874 - Val Acc: 93.64%
Epoch [09/25] | Train Loss: 0.2229 - Train Acc: 92.60% | Val Loss: 0.2482 - Val Acc: 92.76%
Epoch [10/25] | Train Loss: 0.1948 - Train Acc: 93.41% | Val Loss: 0.1483 - Val Acc: 95.32%
Epoch [11/25] | Train Loss: 0.1767 - Train Acc: 93.90% | Val Loss: 0.1402 - Val Acc: 95.46%
Epoch [12/25] | Train Loss: 0.1783 - Train Acc: 94.28% | Val Loss: 0.1999 - Val Acc: 94.22%
Epoch [13/25] | Train Loss: 0.1758 - Train Acc: 94.21% | Val Loss: 0.2820 - Val Acc: 92.25%
Epoch [14/25] | Train Loss: 0.1539 - Train Acc: 94.95% | Val Loss: 0.1988 - Val Acc: 93.78%
Epoch [15/25] | Train Loss: 0.1460 - Train Acc: 95.34% | Val Loss: 0.2397 - Val Acc: 91.66%
Epoch [16/25] | Train Loss: 0.1496 - Train Acc: 95.17% | Val Loss: 0.1913 - Val Acc: 94.59%
Epoch [17/25] | Train Loss: 0.1300 - Train Acc: 95.68% | Val Loss: 0.2430 - Val Acc: 92.61%
Epoch [18/25] | Train Loss: 0.1336 - Train Acc: 95.64% | Val Loss: 0.1550 - Val Acc: 95.10%
Epoch [19/25] | Train Loss: 0.1240 - Train Acc: 96.00% | Val Loss: 0.1410 - Val Acc: 95.25%
Epoch [20/25] | Train Loss: 0.1187 - Train Acc: 95.99% | Val Loss: 0.2332 - Val Acc: 92.54%
Epoch [21/25] | Train Loss: 0.1397 - Train Acc: 95.54% | Val Loss: 0.1529 - Val Acc: 95.61%
Epoch [22/25] | Train Loss: 0.1096 - Train Acc: 96.58% | Val Loss: 0.1589 - Val Acc: 95.17%
Epoch [23/25] | Train Loss: 0.0991 - Train Acc: 96.68% | Val Loss: 0.1459 - Val Acc: 96.05%
Epoch [24/25] | Train Loss: 0.1154 - Train Acc: 96.43% | Val Loss: 0.1439 - Val Acc: 95.76%
Epoch [25/25] | Train Loss: 0.1258 - Train Acc: 96.11% | Val Loss: 0.1439 - Val Acc: 96.85%
--------------------------------------------------
Training Complete!



--------------------------VGG16 Model Trainin for cells dataset-------------------------------

Next I moved to VGG16 model for the same dataset cells, and just updating model in config.json file and running got one runtime error regarding shape mismatch:R untimeError: mat1 and mat2 shapes cannot be multiplied (32x4608 and 4068x1024). On resolving it and training for 5 epochs , I got following results:
 Training executing on device: cpu

 Starting Training Routine...
--------------------------------------------------
Epoch [01/05] | Train Loss: 2.1427 - Train Acc: 26.65% | Val Loss: 1.7201 - Val Acc: 32.41%
Epoch [02/05] | Train Loss: 1.7212 - Train Acc: 31.94% | Val Loss: 1.6708 - Val Acc: 32.19%
Epoch [03/05] | Train Loss: 1.7765 - Train Acc: 29.16% | Val Loss: 1.6905 - Val Acc: 32.41%
Epoch [04/05] | Train Loss: 1.7525 - Train Acc: 29.84% | Val Loss: 1.7218 - Val Acc: 30.43%
Epoch [05/05] | Train Loss: 1.7294 - Train Acc: 30.33% | Val Loss: 1.6634 - Val Acc: 32.55%
--------------------------------------------------
Training Complete!

By keeping dropout_rate to 0.5 and learning rate to 0.001 , i got the following results:
Training executing on device: cpu

 Starting Training Routine...
--------------------------------------------------
Epoch [01/05] | Train Loss: 1.2826 - Train Acc: 52.46% | Val Loss: 0.7528 - Val Acc: 69.35%
Epoch [02/05] | Train Loss: 0.6560 - Train Acc: 77.25% | Val Loss: 2.5878 - Val Acc: 61.08%
Epoch [03/05] | Train Loss: 0.5186 - Train Acc: 82.61% | Val Loss: 0.4877 - Val Acc: 85.00%
Epoch [04/05] | Train Loss: 0.4488 - Train Acc: 85.15% | Val Loss: 3.1619 - Val Acc: 43.96%
Epoch [05/05] | Train Loss: 0.3740 - Train Acc: 87.83% | Val Loss: 0.2598 - Val Acc: 90.86%
--------------------------------------------------
Training Complete!


After keeping drop out rate to 0.5 and increasing epochs to 25 for cells dataset - VGG16 Model and testing on gpu with configurations  "DATA":"cells","DATA_PATH":"Data","MODEL":"VGG16","CHANNELS": 3, "NUM_CLASSES":8,"BATCH_SIZE": 32,"LEARNING_RATE": 0.001,"EPOCHS": 25,"DROPOUT_RATE" : 0.5, "ACTIVATION_STR" : "ReLU", 
I got the following results which crossed the baseline accuracy:
Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 1.6281 - Train Acc: 35.54% | Val Loss: 1.5535 - Val Acc: 36.80%
Epoch [02/25] | Train Loss: 1.2307 - Train Acc: 52.80% | Val Loss: 1.1126 - Val Acc: 60.57%
Epoch [03/25] | Train Loss: 0.9090 - Train Acc: 64.76% | Val Loss: 0.7603 - Val Acc: 70.89%
Epoch [04/25] | Train Loss: 0.7478 - Train Acc: 71.06% | Val Loss: 0.6713 - Val Acc: 74.62%
Epoch [05/25] | Train Loss: 0.6307 - Train Acc: 75.34% | Val Loss: 0.7010 - Val Acc: 71.40%
Epoch [06/25] | Train Loss: 0.5946 - Train Acc: 77.80% | Val Loss: 1.9603 - Val Acc: 56.84%
Epoch [07/25] | Train Loss: 0.5808 - Train Acc: 78.69% | Val Loss: 0.4772 - Val Acc: 80.32%
Epoch [08/25] | Train Loss: 0.4423 - Train Acc: 83.68% | Val Loss: 0.3621 - Val Acc: 85.81%
Epoch [09/25] | Train Loss: 0.5112 - Train Acc: 84.97% | Val Loss: 0.3298 - Val Acc: 88.44%
Epoch [10/25] | Train Loss: 0.4073 - Train Acc: 86.79% | Val Loss: 0.2454 - Val Acc: 92.32%
Epoch [11/25] | Train Loss: 0.3522 - Train Acc: 89.38% | Val Loss: 0.2299 - Val Acc: 93.34%
Epoch [12/25] | Train Loss: 0.3046 - Train Acc: 90.73% | Val Loss: 0.1955 - Val Acc: 92.54%
Epoch [13/25] | Train Loss: 0.3166 - Train Acc: 90.82% | Val Loss: 0.2330 - Val Acc: 92.54%
Epoch [14/25] | Train Loss: 0.3560 - Train Acc: 90.09% | Val Loss: 0.2666 - Val Acc: 91.37%
Epoch [15/25] | Train Loss: 0.2717 - Train Acc: 92.25% | Val Loss: 0.1487 - Val Acc: 95.76%
Epoch [16/25] | Train Loss: 0.2124 - Train Acc: 93.59% | Val Loss: 0.1689 - Val Acc: 95.61%
Epoch [17/25] | Train Loss: 0.1997 - Train Acc: 93.85% | Val Loss: 0.1459 - Val Acc: 95.03%
Epoch [18/25] | Train Loss: 0.2259 - Train Acc: 93.50% | Val Loss: 0.1164 - Val Acc: 96.56%
Epoch [19/25] | Train Loss: 0.1925 - Train Acc: 94.28% | Val Loss: 0.1146 - Val Acc: 96.78%
Epoch [20/25] | Train Loss: 0.1676 - Train Acc: 94.89% | Val Loss: 0.1503 - Val Acc: 95.39%
Epoch [21/25] | Train Loss: 0.1787 - Train Acc: 95.16% | Val Loss: 0.1267 - Val Acc: 95.83%
Epoch [22/25] | Train Loss: 0.2677 - Train Acc: 93.96% | Val Loss: 0.1414 - Val Acc: 95.83%
Epoch [23/25] | Train Loss: 0.1915 - Train Acc: 94.90% | Val Loss: 0.0942 - Val Acc: 97.37%
Epoch [24/25] | Train Loss: 0.1368 - Train Acc: 96.11% | Val Loss: 0.1078 - Val Acc: 96.78%
Epoch [25/25] | Train Loss: 0.1447 - Train Acc: 96.02% | Val Loss: 0.1229 - Val Acc: 96.56%
--------------------------------------------------
Training Complete!


-----------------------------ResNet training for cells dataset--------------------------------
âfter just updating the model and setting same configurations,  "MODEL":"ResNet18","CHANNELS": 3,"NUM_CLASSES": 8,"BATCH_SIZE": 32,"LEARNING_RATE": 0.001,"EPOCHS": 25,"DROPOUT_RATE" : 0.5,
"ACTIVATION_STR" : "ReLU"

Recieved following results:


 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 0.4528 - Train Acc: 83.85% | Val Loss: 0.1971 - Val Acc: 92.61%
Epoch [02/25] | Train Loss: 0.2408 - Train Acc: 91.71% | Val Loss: 0.1755 - Val Acc: 93.78%
Epoch [03/25] | Train Loss: 0.1871 - Train Acc: 93.75% | Val Loss: 0.2726 - Val Acc: 90.42%
Epoch [04/25] | Train Loss: 0.1602 - Train Acc: 94.56% | Val Loss: 0.1310 - Val Acc: 95.03%
Epoch [05/25] | Train Loss: 0.1404 - Train Acc: 95.26% | Val Loss: 0.6481 - Val Acc: 79.74%
Epoch [06/25] | Train Loss: 0.1225 - Train Acc: 95.81% | Val Loss: 0.1220 - Val Acc: 95.83%
Epoch [07/25] | Train Loss: 0.1136 - Train Acc: 96.19% | Val Loss: 0.1805 - Val Acc: 93.12%
Epoch [08/25] | Train Loss: 0.1040 - Train Acc: 96.62% | Val Loss: 0.1285 - Val Acc: 96.20%
Epoch [09/25] | Train Loss: 0.0850 - Train Acc: 97.06% | Val Loss: 0.1167 - Val Acc: 95.90%
Epoch [10/25] | Train Loss: 0.0906 - Train Acc: 97.04% | Val Loss: 0.1888 - Val Acc: 93.49%
Epoch [11/25] | Train Loss: 0.0894 - Train Acc: 96.86% | Val Loss: 0.0781 - Val Acc: 97.66%
Epoch [12/25] | Train Loss: 0.0730 - Train Acc: 97.61% | Val Loss: 0.0830 - Val Acc: 97.29%
Epoch [13/25] | Train Loss: 0.0792 - Train Acc: 97.20% | Val Loss: 0.0980 - Val Acc: 96.78%
Epoch [14/25] | Train Loss: 0.0624 - Train Acc: 97.76% | Val Loss: 0.1203 - Val Acc: 96.27%
Epoch [15/25] | Train Loss: 0.0700 - Train Acc: 97.59% | Val Loss: 0.8575 - Val Acc: 80.83%
Epoch [16/25] | Train Loss: 0.0630 - Train Acc: 97.89% | Val Loss: 0.0526 - Val Acc: 98.46%
Epoch [17/25] | Train Loss: 0.0529 - Train Acc: 98.02% | Val Loss: 0.7991 - Val Acc: 86.61%
Epoch [18/25] | Train Loss: 0.0475 - Train Acc: 98.25% | Val Loss: 0.2015 - Val Acc: 93.86%
Epoch [19/25] | Train Loss: 0.0505 - Train Acc: 98.28% | Val Loss: 0.0848 - Val Acc: 97.00%
Epoch [20/25] | Train Loss: 0.0469 - Train Acc: 98.24% | Val Loss: 0.0696 - Val Acc: 98.02%
Epoch [21/25] | Train Loss: 0.0476 - Train Acc: 98.46% | Val Loss: 0.1247 - Val Acc: 95.61%
Epoch [22/25] | Train Loss: 0.0317 - Train Acc: 98.92% | Val Loss: 0.0977 - Val Acc: 97.51%
Epoch [23/25] | Train Loss: 0.0313 - Train Acc: 98.88% | Val Loss: 0.1316 - Val Acc: 95.83%
Epoch [24/25] | Train Loss: 0.0304 - Train Acc: 98.98% | Val Loss: 0.0577 - Val Acc: 98.32%
Epoch [25/25] | Train Loss: 0.0388 - Train Acc: 98.69% | Val Loss: 0.1612 - Val Acc: 95.46%
--------------------------------------------------
Training Complete!



------------------------------Summary---------------------------
Standard configurations for all three models after individual training for cells.pt dataset:
{
    "DATA": "chest",
    "DATA_PATH": "Data",
    "MODEL": model_name,
    "CHANNELS": 3,
    "NUM_CLASSES": 8,
    "BATCH_SIZE": 32,
    "LEARNING_RATE": 0.001,
    "EPOCHS": 25,
    "DROPOUT_RATE" : 0.5,
    "ACTIVATION_STR" : "ReLU"
}


---------------------Training AlexNet model for chest.pt dataset---------------------
with the same configurations "DATA":"chest",  "CHANNELS": 1,"NUM_CLASSES": 2, "BATCH_SIZE": 32,"LEARNING_RATE": 0.001,"EPOCHS": 25,"DROPOUT_RATE" : 0.5,"ACTIVATION_STR" : "ReLU", but num_classes=2,

ran epochs and got following results:

 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 0.5372 - Train Acc: 79.57% | Val Loss: 0.1863 - Val Acc: 91.20%
Epoch [02/25] | Train Loss: 0.1694 - Train Acc: 93.46% | Val Loss: 0.1289 - Val Acc: 95.79%
Epoch [03/25] | Train Loss: 0.1295 - Train Acc: 95.37% | Val Loss: 0.1377 - Val Acc: 95.41%
Epoch [04/25] | Train Loss: 0.1210 - Train Acc: 95.77% | Val Loss: 0.1322 - Val Acc: 95.79%
Epoch [05/25] | Train Loss: 0.1485 - Train Acc: 94.03% | Val Loss: 0.1168 - Val Acc: 95.60%
Epoch [06/25] | Train Loss: 0.1050 - Train Acc: 95.99% | Val Loss: 0.0753 - Val Acc: 96.37%
Epoch [07/25] | Train Loss: 0.0903 - Train Acc: 96.35% | Val Loss: 0.1850 - Val Acc: 94.07%
Epoch [08/25] | Train Loss: 0.0708 - Train Acc: 97.13% | Val Loss: 0.0867 - Val Acc: 96.94%
Epoch [09/25] | Train Loss: 0.0690 - Train Acc: 97.43% | Val Loss: 0.0857 - Val Acc: 96.75%
Epoch [10/25] | Train Loss: 0.0583 - Train Acc: 97.73% | Val Loss: 0.0751 - Val Acc: 96.56%
Epoch [11/25] | Train Loss: 0.0776 - Train Acc: 97.58% | Val Loss: 0.0802 - Val Acc: 96.56%
Epoch [12/25] | Train Loss: 0.0534 - Train Acc: 98.32% | Val Loss: 0.0777 - Val Acc: 97.51%
Epoch [13/25] | Train Loss: 0.0618 - Train Acc: 97.92% | Val Loss: 0.0733 - Val Acc: 97.71%
Epoch [14/25] | Train Loss: 0.0412 - Train Acc: 98.56% | Val Loss: 0.4003 - Val Acc: 89.87%
Epoch [15/25] | Train Loss: 0.0477 - Train Acc: 98.24% | Val Loss: 0.1682 - Val Acc: 94.26%
Epoch [16/25] | Train Loss: 0.0491 - Train Acc: 98.09% | Val Loss: 0.0907 - Val Acc: 96.56%
Epoch [17/25] | Train Loss: 0.0344 - Train Acc: 98.79% | Val Loss: 0.0851 - Val Acc: 97.71%
Epoch [18/25] | Train Loss: 0.0284 - Train Acc: 98.90% | Val Loss: 0.0974 - Val Acc: 96.94%
Epoch [19/25] | Train Loss: 0.0509 - Train Acc: 98.45% | Val Loss: 0.0884 - Val Acc: 96.18%
Epoch [20/25] | Train Loss: 0.0284 - Train Acc: 99.02% | Val Loss: 0.1155 - Val Acc: 96.94%
Epoch [21/25] | Train Loss: 0.0399 - Train Acc: 98.68% | Val Loss: 0.0577 - Val Acc: 97.71%
Epoch [22/25] | Train Loss: 0.0263 - Train Acc: 99.04% | Val Loss: 0.0804 - Val Acc: 96.56%
Epoch [23/25] | Train Loss: 0.0383 - Train Acc: 98.75% | Val Loss: 0.0720 - Val Acc: 98.09%
Epoch [24/25] | Train Loss: 0.0286 - Train Acc: 99.17% | Val Loss: 0.0969 - Val Acc: 97.51%
Epoch [25/25] | Train Loss: 0.0179 - Train Acc: 99.45% | Val Loss: 0.1220 - Val Acc: 97.51%
--------------------------------------------------
Training Complete!

----------------------------Training VGG16 model for chest.pt dataset--------------------
Got these results with same configurations , just updating the model to VGG16

 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 0.2714 - Train Acc: 90.38% | Val Loss: 0.2008 - Val Acc: 92.35%
Epoch [02/25] | Train Loss: 0.1355 - Train Acc: 95.18% | Val Loss: 0.1310 - Val Acc: 95.98%
Epoch [03/25] | Train Loss: 0.1213 - Train Acc: 95.52% | Val Loss: 0.2564 - Val Acc: 89.87%
Epoch [04/25] | Train Loss: 0.1660 - Train Acc: 94.39% | Val Loss: 0.3076 - Val Acc: 89.29%
Epoch [05/25] | Train Loss: 0.1525 - Train Acc: 94.95% | Val Loss: 0.0805 - Val Acc: 97.90%
Epoch [06/25] | Train Loss: 0.1019 - Train Acc: 96.14% | Val Loss: 0.0859 - Val Acc: 97.71%
Epoch [07/25] | Train Loss: 0.0800 - Train Acc: 97.01% | Val Loss: 0.0986 - Val Acc: 97.13%
Epoch [08/25] | Train Loss: 0.0772 - Train Acc: 97.32% | Val Loss: 0.0731 - Val Acc: 97.71%
Epoch [09/25] | Train Loss: 0.0960 - Train Acc: 97.07% | Val Loss: 0.0639 - Val Acc: 97.90%
Epoch [10/25] | Train Loss: 0.0749 - Train Acc: 97.47% | Val Loss: 0.2924 - Val Acc: 93.31%
Epoch [11/25] | Train Loss: 0.1646 - Train Acc: 94.86% | Val Loss: 0.1246 - Val Acc: 96.37%
Epoch [12/25] | Train Loss: 0.1194 - Train Acc: 96.16% | Val Loss: 0.0735 - Val Acc: 97.13%
Epoch [13/25] | Train Loss: 0.0812 - Train Acc: 97.24% | Val Loss: 0.1267 - Val Acc: 95.79%
Epoch [14/25] | Train Loss: 0.0689 - Train Acc: 97.69% | Val Loss: 0.1460 - Val Acc: 96.56%
Epoch [15/25] | Train Loss: 0.0829 - Train Acc: 97.43% | Val Loss: 0.0930 - Val Acc: 96.37%
Epoch [16/25] | Train Loss: 0.0546 - Train Acc: 97.79% | Val Loss: 0.0998 - Val Acc: 96.94%
Epoch [17/25] | Train Loss: 0.0623 - Train Acc: 97.92% | Val Loss: 0.0785 - Val Acc: 97.32%
Epoch [18/25] | Train Loss: 0.0499 - Train Acc: 98.07% | Val Loss: 0.0952 - Val Acc: 96.94%
Epoch [19/25] | Train Loss: 0.0368 - Train Acc: 98.70% | Val Loss: 0.2358 - Val Acc: 95.22%
Epoch [20/25] | Train Loss: 0.0425 - Train Acc: 98.51% | Val Loss: 0.0900 - Val Acc: 97.71%
Epoch [21/25] | Train Loss: 0.0393 - Train Acc: 98.39% | Val Loss: 0.0746 - Val Acc: 97.51%
Epoch [22/25] | Train Loss: 0.0770 - Train Acc: 98.11% | Val Loss: 0.1019 - Val Acc: 96.18%
Epoch [23/25] | Train Loss: 0.0654 - Train Acc: 97.37% | Val Loss: 0.1109 - Val Acc: 98.09%
Epoch [24/25] | Train Loss: 0.0495 - Train Acc: 98.56% | Val Loss: 0.0731 - Val Acc: 97.32%
Epoch [25/25] | Train Loss: 0.0398 - Train Acc: 98.75% | Val Loss: 0.1738 - Val Acc: 96.37%
--------------------------------------------------
Training Complete!

-------------------------------training ResNet18 model for chest.pt dataset--------------------------------
with same configurations, just updating the model, gave following results:

 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 0.2594 - Train Acc: 89.87% | Val Loss: 0.1902 - Val Acc: 92.73%
Epoch [02/25] | Train Loss: 0.1599 - Train Acc: 93.95% | Val Loss: 0.2652 - Val Acc: 87.57%
Epoch [03/25] | Train Loss: 0.1225 - Train Acc: 95.37% | Val Loss: 0.1238 - Val Acc: 95.03%
Epoch [04/25] | Train Loss: 0.1076 - Train Acc: 95.92% | Val Loss: 0.1539 - Val Acc: 95.03%
Epoch [05/25] | Train Loss: 0.0926 - Train Acc: 96.86% | Val Loss: 0.1028 - Val Acc: 95.41%
Epoch [06/25] | Train Loss: 0.0880 - Train Acc: 96.69% | Val Loss: 0.0895 - Val Acc: 95.98%
Epoch [07/25] | Train Loss: 0.0918 - Train Acc: 96.79% | Val Loss: 0.1226 - Val Acc: 95.79%
Epoch [08/25] | Train Loss: 0.0708 - Train Acc: 97.64% | Val Loss: 0.1339 - Val Acc: 95.03%
Epoch [09/25] | Train Loss: 0.0779 - Train Acc: 96.67% | Val Loss: 0.1284 - Val Acc: 94.26%
Epoch [10/25] | Train Loss: 0.0766 - Train Acc: 97.03% | Val Loss: 0.0804 - Val Acc: 96.37%
Epoch [11/25] | Train Loss: 0.0792 - Train Acc: 97.18% | Val Loss: 0.1050 - Val Acc: 95.41%
Epoch [12/25] | Train Loss: 0.0539 - Train Acc: 97.90% | Val Loss: 0.0866 - Val Acc: 97.32%
Epoch [13/25] | Train Loss: 0.0491 - Train Acc: 98.15% | Val Loss: 0.0665 - Val Acc: 97.90%
Epoch [14/25] | Train Loss: 0.0423 - Train Acc: 98.45% | Val Loss: 0.0678 - Val Acc: 97.13%
Epoch [15/25] | Train Loss: 0.0439 - Train Acc: 98.15% | Val Loss: 0.2004 - Val Acc: 95.22%
Epoch [16/25] | Train Loss: 0.0468 - Train Acc: 98.26% | Val Loss: 0.2959 - Val Acc: 91.97%
Epoch [17/25] | Train Loss: 0.0456 - Train Acc: 98.11% | Val Loss: 0.0799 - Val Acc: 97.13%
Epoch [18/25] | Train Loss: 0.0349 - Train Acc: 98.66% | Val Loss: 0.0906 - Val Acc: 97.32%
Epoch [19/25] | Train Loss: 0.0290 - Train Acc: 99.04% | Val Loss: 0.1347 - Val Acc: 97.32%
Epoch [20/25] | Train Loss: 0.0186 - Train Acc: 99.28% | Val Loss: 0.1021 - Val Acc: 96.94%
Epoch [21/25] | Train Loss: 0.0316 - Train Acc: 99.00% | Val Loss: 0.1233 - Val Acc: 95.60%
Epoch [22/25] | Train Loss: 0.0179 - Train Acc: 99.43% | Val Loss: 0.1443 - Val Acc: 96.56%
Epoch [23/25] | Train Loss: 0.0655 - Train Acc: 97.60% | Val Loss: 0.1055 - Val Acc: 96.56%
Epoch [24/25] | Train Loss: 0.0215 - Train Acc: 99.21% | Val Loss: 0.0807 - Val Acc: 97.32%
Epoch [25/25] | Train Loss: 0.0147 - Train Acc: 99.47% | Val Loss: 0.1479 - Val Acc: 96.94%
--------------------------------------------------
Training Complete!

---------------------Summary---------------------------
optimal Configurations:
{
    "DATA": "chest",
    "DATA_PATH": "Data",
    "MODEL": model_name,
    "CHANNELS": 1,
    "NUM_CLASSES": 2,
    "BATCH_SIZE": 32,
    "LEARNING_RATE": 0.001,
    "EPOCHS": 25,
    "DROPOUT_RATE" : 0.5,
    "ACTIVATION_STR" : "ReLU"
}

-------------------------------training AlexNet for lesions.pt dataset-------------------------------

With same configurations, but no. of input channels 3 and number of classes=7, got the following results (exceeding baseline of 67%).
Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 1.0797 - Train Acc: 65.20% | Val Loss: 0.9263 - Val Acc: 66.67%
Epoch [02/25] | Train Loss: 0.9014 - Train Acc: 67.33% | Val Loss: 0.8792 - Val Acc: 67.29%
Epoch [03/25] | Train Loss: 0.8673 - Train Acc: 68.21% | Val Loss: 0.8717 - Val Acc: 67.92%
Epoch [04/25] | Train Loss: 0.8488 - Train Acc: 68.97% | Val Loss: 0.8518 - Val Acc: 67.42%
Epoch [05/25] | Train Loss: 0.8305 - Train Acc: 69.52% | Val Loss: 0.7956 - Val Acc: 70.54%
Epoch [06/25] | Train Loss: 0.8192 - Train Acc: 70.08% | Val Loss: 0.7891 - Val Acc: 70.41%
Epoch [07/25] | Train Loss: 0.7836 - Train Acc: 70.98% | Val Loss: 0.7896 - Val Acc: 72.41%
Epoch [08/25] | Train Loss: 0.7754 - Train Acc: 70.79% | Val Loss: 0.7934 - Val Acc: 69.91%
Epoch [09/25] | Train Loss: 0.7525 - Train Acc: 72.20% | Val Loss: 0.7479 - Val Acc: 72.66%
Epoch [10/25] | Train Loss: 0.7353 - Train Acc: 72.96% | Val Loss: 0.7372 - Val Acc: 72.03%
Epoch [11/25] | Train Loss: 0.7304 - Train Acc: 73.05% | Val Loss: 0.7747 - Val Acc: 71.29%
Epoch [12/25] | Train Loss: 0.7183 - Train Acc: 73.66% | Val Loss: 0.7291 - Val Acc: 73.53%
Epoch [13/25] | Train Loss: 0.6986 - Train Acc: 74.43% | Val Loss: 0.7308 - Val Acc: 73.41%
Epoch [14/25] | Train Loss: 0.6807 - Train Acc: 74.74% | Val Loss: 0.7479 - Val Acc: 73.53%
Epoch [15/25] | Train Loss: 0.6829 - Train Acc: 75.20% | Val Loss: 0.7223 - Val Acc: 73.28%
Epoch [16/25] | Train Loss: 0.6668 - Train Acc: 75.35% | Val Loss: 0.6807 - Val Acc: 75.16%
Epoch [17/25] | Train Loss: 0.6575 - Train Acc: 75.81% | Val Loss: 0.6950 - Val Acc: 74.03%
Epoch [18/25] | Train Loss: 0.6533 - Train Acc: 76.14% | Val Loss: 0.7130 - Val Acc: 73.41%
Epoch [19/25] | Train Loss: 0.6384 - Train Acc: 76.40% | Val Loss: 0.6895 - Val Acc: 74.66%
Epoch [20/25] | Train Loss: 0.6242 - Train Acc: 77.03% | Val Loss: 0.6963 - Val Acc: 74.03%
Epoch [21/25] | Train Loss: 0.6100 - Train Acc: 77.69% | Val Loss: 0.7123 - Val Acc: 73.16%
Epoch [22/25] | Train Loss: 0.6087 - Train Acc: 78.07% | Val Loss: 0.6741 - Val Acc: 75.28%
Epoch [23/25] | Train Loss: 0.6007 - Train Acc: 78.08% | Val Loss: 0.7113 - Val Acc: 74.03%
Epoch [24/25] | Train Loss: 0.5774 - Train Acc: 78.43% | Val Loss: 0.7206 - Val Acc: 73.28%
Epoch [25/25] | Train Loss: 0.5773 - Train Acc: 78.83% | Val Loss: 0.7328 - Val Acc: 74.41%
--------------------------------------------------
Training Complete!


----------------------------------training VGG16 Model with lesions.pt dataset-------------------------
with same configuration, got the following results:
Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 1.0875 - Train Acc: 66.43% | Val Loss: 1.3318 - Val Acc: 65.92%
Epoch [02/25] | Train Loss: 0.9665 - Train Acc: 67.24% | Val Loss: 0.9833 - Val Acc: 65.92%
Epoch [03/25] | Train Loss: 0.9403 - Train Acc: 66.90% | Val Loss: 0.9312 - Val Acc: 65.92%
Epoch [04/25] | Train Loss: 0.9036 - Train Acc: 67.83% | Val Loss: 0.9408 - Val Acc: 67.92%
Epoch [05/25] | Train Loss: 0.8999 - Train Acc: 67.53% | Val Loss: 0.9512 - Val Acc: 65.92%
Epoch [06/25] | Train Loss: 0.8869 - Train Acc: 68.11% | Val Loss: 0.9102 - Val Acc: 67.67%
Epoch [07/25] | Train Loss: 0.8637 - Train Acc: 68.41% | Val Loss: 0.8476 - Val Acc: 68.66%
Epoch [08/25] | Train Loss: 0.8676 - Train Acc: 68.41% | Val Loss: 0.8428 - Val Acc: 68.79%
Epoch [09/25] | Train Loss: 0.8479 - Train Acc: 68.53% | Val Loss: 0.8275 - Val Acc: 67.67%
Epoch [10/25] | Train Loss: 0.8571 - Train Acc: 68.64% | Val Loss: 0.8759 - Val Acc: 67.29%
Epoch [11/25] | Train Loss: 0.8404 - Train Acc: 68.51% | Val Loss: 0.8229 - Val Acc: 68.16%
Epoch [12/25] | Train Loss: 0.8300 - Train Acc: 69.22% | Val Loss: 0.8318 - Val Acc: 69.79%
Epoch [13/25] | Train Loss: 0.8283 - Train Acc: 69.66% | Val Loss: 0.8295 - Val Acc: 69.16%
Epoch [14/25] | Train Loss: 0.8131 - Train Acc: 70.45% | Val Loss: 0.8319 - Val Acc: 69.54%
Epoch [15/25] | Train Loss: 0.8133 - Train Acc: 70.36% | Val Loss: 0.8037 - Val Acc: 69.29%
Epoch [16/25] | Train Loss: 0.7970 - Train Acc: 70.45% | Val Loss: 0.7734 - Val Acc: 70.91%
Epoch [17/25] | Train Loss: 0.7978 - Train Acc: 70.50% | Val Loss: 0.7996 - Val Acc: 72.16%
Epoch [18/25] | Train Loss: 0.7866 - Train Acc: 70.93% | Val Loss: 0.7747 - Val Acc: 70.54%
Epoch [19/25] | Train Loss: 0.7847 - Train Acc: 71.55% | Val Loss: 0.8527 - Val Acc: 70.04%
Epoch [20/25] | Train Loss: 0.7714 - Train Acc: 71.60% | Val Loss: 0.7851 - Val Acc: 72.91%
Epoch [21/25] | Train Loss: 0.7856 - Train Acc: 71.52% | Val Loss: 0.7779 - Val Acc: 71.79%
Epoch [22/25] | Train Loss: 0.7540 - Train Acc: 72.46% | Val Loss: 0.7759 - Val Acc: 74.53%
Epoch [23/25] | Train Loss: 0.7605 - Train Acc: 72.26% | Val Loss: 0.7500 - Val Acc: 73.66%
Epoch [24/25] | Train Loss: 0.7391 - Train Acc: 72.74% | Val Loss: 0.7687 - Val Acc: 73.41%
Epoch [25/25] | Train Loss: 0.7427 - Train Acc: 72.52% | Val Loss: 0.7573 - Val Acc: 73.28%
--------------------------------------------------
Training Complete!

-----------------training ResNet model with lesions.pt dataset-------------------------


 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 0.9448 - Train Acc: 67.10% | Val Loss: 0.9730 - Val Acc: 66.17%
Epoch [02/25] | Train Loss: 0.8784 - Train Acc: 68.11% | Val Loss: 0.9511 - Val Acc: 62.92%
Epoch [03/25] | Train Loss: 0.8473 - Train Acc: 68.55% | Val Loss: 0.9291 - Val Acc: 68.16%
Epoch [04/25] | Train Loss: 0.7982 - Train Acc: 70.34% | Val Loss: 0.7477 - Val Acc: 71.91%
Epoch [05/25] | Train Loss: 0.7790 - Train Acc: 70.98% | Val Loss: 0.7506 - Val Acc: 72.53%
Epoch [06/25] | Train Loss: 0.7592 - Train Acc: 71.76% | Val Loss: 1.4457 - Val Acc: 53.56%
Epoch [07/25] | Train Loss: 0.7389 - Train Acc: 72.48% | Val Loss: 1.1427 - Val Acc: 62.42%
Epoch [08/25] | Train Loss: 0.7290 - Train Acc: 73.17% | Val Loss: 0.7115 - Val Acc: 73.16%
Epoch [09/25] | Train Loss: 0.7123 - Train Acc: 73.87% | Val Loss: 0.7331 - Val Acc: 71.91%
Epoch [10/25] | Train Loss: 0.6902 - Train Acc: 74.14% | Val Loss: 0.7274 - Val Acc: 72.41%
Epoch [11/25] | Train Loss: 0.6790 - Train Acc: 74.74% | Val Loss: 0.7597 - Val Acc: 72.53%
Epoch [12/25] | Train Loss: 0.6713 - Train Acc: 75.13% | Val Loss: 0.6742 - Val Acc: 74.66%
Epoch [13/25] | Train Loss: 0.6592 - Train Acc: 75.74% | Val Loss: 0.7485 - Val Acc: 71.04%
Epoch [14/25] | Train Loss: 0.6537 - Train Acc: 75.72% | Val Loss: 0.6774 - Val Acc: 74.28%
Epoch [15/25] | Train Loss: 0.6378 - Train Acc: 76.50% | Val Loss: 0.6923 - Val Acc: 74.66%
Epoch [16/25] | Train Loss: 0.6283 - Train Acc: 76.71% | Val Loss: 0.7024 - Val Acc: 74.66%
Epoch [17/25] | Train Loss: 0.6122 - Train Acc: 76.82% | Val Loss: 0.7352 - Val Acc: 73.03%
Epoch [18/25] | Train Loss: 0.5990 - Train Acc: 77.97% | Val Loss: 0.6808 - Val Acc: 76.78%
Epoch [19/25] | Train Loss: 0.5774 - Train Acc: 78.12% | Val Loss: 0.6806 - Val Acc: 76.15%
Epoch [20/25] | Train Loss: 0.5698 - Train Acc: 79.03% | Val Loss: 0.6992 - Val Acc: 75.66%
Epoch [21/25] | Train Loss: 0.5471 - Train Acc: 79.48% | Val Loss: 0.6853 - Val Acc: 74.78%
Epoch [22/25] | Train Loss: 0.5212 - Train Acc: 80.55% | Val Loss: 0.7629 - Val Acc: 72.78%
Epoch [23/25] | Train Loss: 0.5042 - Train Acc: 80.89% | Val Loss: 0.7747 - Val Acc: 75.78%
Epoch [24/25] | Train Loss: 0.4659 - Train Acc: 82.08% | Val Loss: 0.7795 - Val Acc: 74.28%
Epoch [25/25] | Train Loss: 0.4242 - Train Acc: 84.34% | Val Loss: 0.8131 - Val Acc: 74.53%
--------------------------------------------------
Training Complete!

-------------Summary---------------
Same configuration as earlier , just change num of channels, num of classes, data to lesions.pt 

{
    "DATA": "lesions",
    "DATA_PATH": "Data",
    "MODEL": model_name,
    "CHANNELS": 3,
    "NUM_CLASSES": 7,
    "BATCH_SIZE": 32,
    "LEARNING_RATE": 0.001,
    "EPOCHS": 25,
    "DROPOUT_RATE" : 0.5,
    "ACTIVATION_STR" : "ReLU"
}


------------------------Training Alexnet for orgs.pt dataset-------------------
got following results with same configuration and no. of input channels as 1 and no. of classes as 11:

 Starting Training Routine...
--------------------------------------------------
Epoch [01/25] | Train Loss: 0.9333 - Train Acc: 67.19% | Val Loss: 0.2953 - Val Acc: 91.54%
Epoch [02/25] | Train Loss: 0.4173 - Train Acc: 86.49% | Val Loss: 0.1510 - Val Acc: 96.42%
Epoch [03/25] | Train Loss: 0.3275 - Train Acc: 89.45% | Val Loss: 0.1183 - Val Acc: 97.01%
Epoch [04/25] | Train Loss: 0.2595 - Train Acc: 91.35% | Val Loss: 0.1520 - Val Acc: 95.57%
Epoch [05/25] | Train Loss: 0.2422 - Train Acc: 91.90% | Val Loss: 0.0929 - Val Acc: 96.94%
Epoch [06/25] | Train Loss: 0.2110 - Train Acc: 93.10% | Val Loss: 0.0903 - Val Acc: 97.33%
Epoch [07/25] | Train Loss: 0.1994 - Train Acc: 93.34% | Val Loss: 0.0780 - Val Acc: 97.33%
Epoch [08/25] | Train Loss: 0.1733 - Train Acc: 94.19% | Val Loss: 0.1009 - Val Acc: 97.07%
Epoch [09/25] | Train Loss: 0.1621 - Train Acc: 94.51% | Val Loss: 0.0508 - Val Acc: 98.50%
Epoch [10/25] | Train Loss: 0.1643 - Train Acc: 94.64% | Val Loss: 0.0509 - Val Acc: 98.11%
Epoch [11/25] | Train Loss: 0.1712 - Train Acc: 94.55% | Val Loss: 0.0427 - Val Acc: 98.18%
Epoch [12/25] | Train Loss: 0.1362 - Train Acc: 95.60% | Val Loss: 0.0656 - Val Acc: 98.57%
Epoch [13/25] | Train Loss: 0.1274 - Train Acc: 95.72% | Val Loss: 0.1581 - Val Acc: 96.09%
Epoch [14/25] | Train Loss: 0.1505 - Train Acc: 95.31% | Val Loss: 0.0666 - Val Acc: 97.92%
Epoch [15/25] | Train Loss: 0.1115 - Train Acc: 96.34% | Val Loss: 0.0315 - Val Acc: 98.89%
Epoch [16/25] | Train Loss: 0.1249 - Train Acc: 96.15% | Val Loss: 0.0604 - Val Acc: 97.79%
Epoch [17/25] | Train Loss: 0.1038 - Train Acc: 96.45% | Val Loss: 0.0531 - Val Acc: 98.63%
Epoch [18/25] | Train Loss: 0.1145 - Train Acc: 96.52% | Val Loss: 0.0418 - Val Acc: 98.57%
Epoch [19/25] | Train Loss: 0.1108 - Train Acc: 96.69% | Val Loss: 0.0420 - Val Acc: 98.83%
Epoch [20/25] | Train Loss: 0.1122 - Train Acc: 96.40% | Val Loss: 0.0546 - Val Acc: 98.50%
Epoch [21/25] | Train Loss: 0.1128 - Train Acc: 96.57% | Val Loss: 0.0830 - Val Acc: 98.18%
Epoch [22/25] | Train Loss: 0.1103 - Train Acc: 96.51% | Val Loss: 0.0618 - Val Acc: 98.37%
Epoch [23/25] | Train Loss: 0.0913 - Train Acc: 97.28% | Val Loss: 0.0579 - Val Acc: 98.50%
Epoch [24/25] | Train Loss: 0.0958 - Train Acc: 97.02% | Val Loss: 0.0860 - Val Acc: 98.11%
Epoch [25/25] | Train Loss: 0.0898 - Train Acc: 97.22% | Val Loss: 0.0718 - Val Acc: 98.57%
--------------------------------------------------
Training Complete!
---------------Summary--------------
optimal configuration :
{
    "DATA": "orgs",
    "DATA_PATH": "Data",
    "MODEL": model_name,
    "CHANNELS": 1,
    "NUM_CLASSES": 11,
    "BATCH_SIZE": 32,
    "LEARNING_RATE": 0.001,
    "EPOCHS": 25,
    "DROPOUT_RATE" : 0.5,
    "ACTIVATION_STR" : "ReLU"
}



Training Complete!



I created a runner_test file for testing all models over all datasets simultaneously and increased epochs to 10 and got the following results :
Training Complete!

==================================================
FINAL RESULTS SUMMARY
==================================================
AlexNet on cells | P: 0.9115 | R: 0.9115 | Val Acc: 91.15% | F1: 0.9115 | Time: 25.6 |Memory: 187.1MB | Latency: 0.060ms/sample
VGG16 on cells | P: 0.9327 | R: 0.9327 | Val Acc: 93.27% | F1: 0.9327 | Time: 83.4 |Memory: 632.9MB | Latency: 0.204ms/sample
ResNet18 on cells | P: 0.8720 | R: 0.8720 | Val Acc: 87.20% | F1: 0.8720 | Time: 135.6 |Memory: 791.0MB | Latency: 0.313ms/sample
AlexNet on chest | P: 0.9713 | R: 0.9713 | Val Acc: 97.13% | F1: 0.9713 | Time: 8.8 |Memory: 213.5MB | Latency: 0.058ms/sample
VGG16 on chest | P: 0.9675 | R: 0.9675 | Val Acc: 96.75% | F1: 0.9675 | Time: 31.2 |Memory: 626.9MB | Latency: 0.199ms/sample
ResNet18 on chest | P: 0.9637 | R: 0.9637 | Val Acc: 96.37% | F1: 0.9637 | Time: 50.9 |Memory: 788.8MB | Latency: 0.303ms/sample
AlexNet on lesions | P: 0.7241 | R: 0.7241 | Val Acc: 72.41% | F1: 0.7241 | Time: 14.9 |Memory: 212.6MB | Latency: 0.071ms/sample
VGG16 on lesions | P: 0.6692 | R: 0.6692 | Val Acc: 66.92% | F1: 0.6692 | Time: 48.9 |Memory: 634.4MB | Latency: 0.207ms/sample
ResNet18 on lesions | P: 0.7341 | R: 0.7341 | Val Acc: 73.41% | F1: 0.7341 | Time: 79.1 |Memory: 789.9MB | Latency: 0.311ms/sample
AlexNet on orgs | P: 0.9844 | R: 0.9844 | Val Acc: 98.44% | F1: 0.9844 | Time: 23.9 |Memory: 212.1MB | Latency: 0.048ms/sample
VGG16 on orgs | P: 0.9772 | R: 0.9772 | Val Acc: 97.72% | F1: 0.9772 | Time: 90.7 |Memory: 630.2MB | Latency: 0.197ms/sample
ResNet18 on orgs | P: 0.9850 | R: 0.9850 | Val Acc: 98.50% | F1: 0.9850 | Time: 148.7 |Memory: 789.0MB | Latency: 0.295ms/sample

==================================================
FINAL RESULTS SUMMARY
==================================================
AlexNet on cells | P: 0.9115 | R: 0.9115 | Val Acc: 91.15% | F1: 0.9115 | Time: 25.6 |Memory: 187.1MB | Latency: 0.060ms/sample
VGG16 on cells | P: 0.9327 | R: 0.9327 | Val Acc: 93.27% | F1: 0.9327 | Time: 83.4 |Memory: 632.9MB | Latency: 0.204ms/sample
ResNet18 on cells | P: 0.8720 | R: 0.8720 | Val Acc: 87.20% | F1: 0.8720 | Time: 135.6 |Memory: 791.0MB | Latency: 0.313ms/sample
AlexNet on chest | P: 0.9713 | R: 0.9713 | Val Acc: 97.13% | F1: 0.9713 | Time: 8.8 |Memory: 213.5MB | Latency: 0.058ms/sample
VGG16 on chest | P: 0.9675 | R: 0.9675 | Val Acc: 96.75% | F1: 0.9675 | Time: 31.2 |Memory: 626.9MB | Latency: 0.199ms/sample
ResNet18 on chest | P: 0.9637 | R: 0.9637 | Val Acc: 96.37% | F1: 0.9637 | Time: 50.9 |Memory: 788.8MB | Latency: 0.303ms/sample
AlexNet on lesions | P: 0.7241 | R: 0.7241 | Val Acc: 72.41% | F1: 0.7241 | Time: 14.9 |Memory: 212.6MB | Latency: 0.071ms/sample
VGG16 on lesions | P: 0.6692 | R: 0.6692 | Val Acc: 66.92% | F1: 0.6692 | Time: 48.9 |Memory: 634.4MB | Latency: 0.207ms/sample
ResNet18 on lesions | P: 0.7341 | R: 0.7341 | Val Acc: 73.41% | F1: 0.7341 | Time: 79.1 |Memory: 789.9MB | Latency: 0.311ms/sample
AlexNet on orgs | P: 0.9844 | R: 0.9844 | Val Acc: 98.44% | F1: 0.9844 | Time: 23.9 |Memory: 212.1MB | Latency: 0.048ms/sample
VGG16 on orgs | P: 0.9772 | R: 0.9772 | Val Acc: 97.72% | F1: 0.9772 | Time: 90.7 |Memory: 630.2MB | Latency: 0.197ms/sample
ResNet18 on orgs | P: 0.9850 | R: 0.9850 | Val Acc: 98.50% | F1: 0.9850 | Time: 148.7 |Memory: 789.0MB | Latency: 0.295ms/sample



---------------------------------------GreenNet network---------------------------------------------------
created a basic green net model runner_test.py file for testing all models on all datasets simultanously  and running it and got the following results with 10 epochs for each :


==================================================
FINAL RESULTS SUMMARY
==================================================
AlexNet on cells | P: 0.9342 | R: 0.9342 | Val Acc: 93.42% | F1: 0.9342 | Time: 55.7 |Memory: 187.1MB | Latency: 0.211ms/sample
VGG16 on cells | P: 0.8808 | R: 0.8808 | Val Acc: 88.08% | F1: 0.8808 | Time: 186.8 |Memory: 632.9MB | Latency: 0.516ms/sample
ResNet18 on cells | P: 0.9151 | R: 0.9151 | Val Acc: 91.51% | F1: 0.9151 | Time: 297.6 |Memory: 791.0MB | Latency: 0.588ms/sample
GreenNet on cells | P: 0.9561 | R: 0.9561 | Val Acc: 95.61% | F1: 0.9561 | Time: 35.8 |Memory: 195.1MB | Latency: 0.185ms/sample
AlexNet on chest | P: 0.9751 | R: 0.9751 | Val Acc: 97.51% | F1: 0.9751 | Time: 17.4 |Memory: 183.0MB | Latency: 0.164ms/sample
VGG16 on chest | P: 0.9675 | R: 0.9675 | Val Acc: 96.75% | F1: 0.9675 | Time: 59.5 |Memory: 630.0MB | Latency: 0.421ms/sample
ResNet18 on chest | P: 0.9732 | R: 0.9732 | Val Acc: 97.32% | F1: 0.9732 | Time: 99.6 |Memory: 790.4MB | Latency: 0.659ms/sample
GreenNet on chest | P: 0.9751 | R: 0.9751 | Val Acc: 97.51% | F1: 0.9751 | Time: 12.2 |Memory: 194.2MB | Latency: 0.169ms/sample
AlexNet on lesions | P: 0.7378 | R: 0.7378 | Val Acc: 73.78% | F1: 0.7378 | Time: 28.9 |Memory: 185.8MB | Latency: 0.207ms/sample
VGG16 on lesions | P: 0.6679 | R: 0.6679 | Val Acc: 66.79% | F1: 0.6679 | Time: 92.4 |Memory: 632.0MB | Latency: 0.431ms/sample
ResNet18 on lesions | P: 0.7278 | R: 0.7278 | Val Acc: 72.78% | F1: 0.7278 | Time: 154.0 |Memory: 789.7MB | Latency: 0.685ms/sample
GreenNet on lesions | P: 0.7091 | R: 0.7091 | Val Acc: 70.91% | F1: 0.7091 | Time: 22.4 |Memory: 194.0MB | Latency: 0.187ms/sample
AlexNet on orgs | P: 0.9818 | R: 0.9818 | Val Acc: 98.18% | F1: 0.9818 | Time: 48.1 |Memory: 185.0MB | Latency: 0.180ms/sample
VGG16 on orgs | P: 0.9785 | R: 0.9785 | Val Acc: 97.85% | F1: 0.9785 | Time: 189.1 |Memory: 628.8MB | Latency: 0.429ms/sample
ResNet18 on orgs | P: 0.9902 | R: 0.9902 | Val Acc: 99.02% | F1: 0.9902 | Time: 311.0 |Memory: 787.9MB | Latency: 0.725ms/sample
GreenNet on orgs | P: 0.9857 | R: 0.9857 | Val Acc: 98.57% | F1: 0.9857 | Time: 40.3 |Memory: 193.7MB | Latency: 0.179ms/sample
