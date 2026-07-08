------------------FOR  TASK-1 ------------------------------------------------------

After keeping configuration values as 

MODEL_SET = ["AlexNet", "VGG16", "ResNet18"]
DATA_PATH = "Data"
BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 15
DROPOUT_RATE = 0.5
ACTIVATION_STR = "ReLU", and testing for all 4 datsets got following results which passed the baseline accuracy as follows:  cells: 90%, chest:
87%, lesions: 67%, orgs: 83%


==================================================
FINAL RESULTS SUMMARY
==================================================
AlexNet on cells | P: 0.9290 | R: 0.9290 | Val Acc: 92.90% | F1: 0.9290 | Time: 81.3 |Memory: 187.1MB | Latency: 0.200ms/sample
VGG16 on cells | P: 0.9364 | R: 0.9364 | Val Acc: 93.64% | F1: 0.9364 | Time: 252.3 |Memory: 632.9MB | Latency: 0.362ms/sample
ResNet18 on cells | P: 0.9788 | R: 0.9788 | Val Acc: 97.88% | F1: 0.9788 | Time: 433.8 |Memory: 791.0MB | Latency: 0.811ms/sample
AlexNet on chest | P: 0.9751 | R: 0.9751 | Val Acc: 97.51% | F1: 0.9751 | Time: 29.7 |Memory: 213.5MB | Latency: 0.244ms/sample
VGG16 on chest | P: 0.9694 | R: 0.9694 | Val Acc: 96.94% | F1: 0.9694 | Time: 108.5 |Memory: 626.9MB | Latency: 0.545ms/sample
ResNet18 on chest | P: 0.9771 | R: 0.9771 | Val Acc: 97.71% | F1: 0.9771 | Time: 178.8 |Memory: 788.8MB | Latency: 0.485ms/sample
AlexNet on lesions | P: 0.7503 | R: 0.7503 | Val Acc: 75.03% | F1: 0.7503 | Time: 45.7 |Memory: 212.6MB | Latency: 0.246ms/sample
VGG16 on lesions | P: 0.6929 | R: 0.6929 | Val Acc: 69.29% | F1: 0.6929 | Time: 167.4 |Memory: 634.4MB | Latency: 0.515ms/sample
ResNet18 on lesions | P: 0.7416 | R: 0.7416 | Val Acc: 74.16% | F1: 0.7416 | Time: 235.1 |Memory: 789.9MB | Latency: 0.560ms/sample
AlexNet on orgs | P: 0.9837 | R: 0.9837 | Val Acc: 98.37% | F1: 0.9837 | Time: 65.6 |Memory: 212.1MB | Latency: 0.102ms/sample
VGG16 on orgs | P: 0.9831 | R: 0.9831 | Val Acc: 98.31% | F1: 0.9831 | Time: 259.5 |Memory: 630.2MB | Latency: 0.489ms/sample
ResNet18 on orgs | P: 0.9870 | R: 0.9870 | Val Acc: 98.70% | F1: 0.9870 | Time: 481.7 |Memory: 789.0MB | Latency: 0.797ms/sample



---------------------   on testing, got the following results:
==================================================
FINAL RESULTS SUMMARY
==================================================
AlexNet on cells | P: 0.9512 | R: 0.9498 | Test Loss: 0.1925 | Test Acc: 95.41% | F1: 0.9497 | Time: 88.8s |Memory: 187.1MB | Latency: 0.123ms/sample
VGG16 on cells | P: 0.9432 | R: 0.9381 | Test Loss: 0.2084 | Test Acc: 94.39% | F1: 0.9393 | Time: 187.9s |Memory: 632.9MB | Latency: 0.237ms/sample
ResNet18 on cells | P: 0.9131 | R: 0.8976 | Test Loss: 0.2330 | Test Acc: 91.93% | F1: 0.8956 | Time: 293.2s |Memory: 791.0MB | Latency: 0.473ms/sample
AlexNet on chest | P: 0.8955 | R: 0.8038 | Test Loss: 1.6440 | Test Acc: 85.10% | F1: 0.8243 | Time: 22.3s |Memory: 213.5MB | Latency: 0.103ms/sample
VGG16 on chest | P: 0.8769 | R: 0.8607 | Test Loss: 0.3551 | Test Acc: 87.82% | F1: 0.8674 | Time: 81.7s |Memory: 626.9MB | Latency: 0.330ms/sample
ResNet18 on chest | P: 0.9034 | R: 0.8282 | Test Loss: 0.4664 | Test Acc: 86.86% | F1: 0.8479 | Time: 108.6s |Memory: 788.8MB | Latency: 0.412ms/sample
AlexNet on lesions | P: 0.4913 | R: 0.4596 | Test Loss: 0.6825 | Test Acc: 74.76% | F1: 0.4646 | Time: 64.9s |Memory: 212.6MB | Latency: 0.201ms/sample
VGG16 on lesions | P: 0.1456 | R: 0.1709 | Test Loss: 1.0294 | Test Acc: 67.83% | F1: 0.1540 | Time: 136.5s |Memory: 634.4MB | Latency: 0.413ms/sample
ResNet18 on lesions | P: 0.4758 | R: 0.4649 | Test Loss: 0.6999 | Test Acc: 73.72% | F1: 0.4594 | Time: 203.2s |Memory: 789.9MB | Latency: 0.490ms/sample
AlexNet on orgs | P: 0.8919 | R: 0.8749 | Test Loss: 0.4835 | Test Acc: 89.33% | F1: 0.8799 | Time: 115.9s |Memory: 212.1MB | Latency: 0.245ms/sample
VGG16 on orgs | P: 0.8803 | R: 0.8681 | Test Loss: 0.4299 | Test Acc: 88.89% | F1: 0.8715 | Time: 232.2s |Memory: 630.2MB | Latency: 0.286ms/sample
ResNet18 on orgs | P: 0.9075 | R: 0.9086 | Test Loss: 0.3075 | Test Acc: 91.72% | F1: 0.9059 | Time: 340.7s |Memory: 789.0MB | Latency: 0.399ms/sample


-----------------------For GreenNet model network--------------------------------------------
created a greennet model with 64 neurons in fully connected layer
=== GreenNet on lesions ===

 Starting Training Routine...
--------------------------------------------------
Epoch [01/15] | Train Loss: 0.9011 - Train Acc: 68.15% | Val Loss: 0.8269 - Val Acc: 70.16% | F1: 0.70
Epoch [02/15] | Train Loss: 0.7827 - Train Acc: 71.11% | Val Loss: 0.7597 - Val Acc: 70.66% | F1: 0.71
Epoch [03/15] | Train Loss: 0.7000 - Train Acc: 74.00% | Val Loss: 0.7678 - Val Acc: 71.41% | F1: 0.71
Epoch [04/15] | Train Loss: 0.6512 - Train Acc: 75.97% | Val Loss: 0.7644 - Val Acc: 72.91% | F1: 0.73
Epoch [05/15] | Train Loss: 0.5773 - Train Acc: 78.73% | Val Loss: 0.7907 - Val Acc: 72.03% | F1: 0.72
Epoch [06/15] | Train Loss: 0.5115 - Train Acc: 80.93% | Val Loss: 0.8079 - Val Acc: 72.91% | F1: 0.73
Epoch [07/15] | Train Loss: 0.4407 - Train Acc: 83.60% | Val Loss: 0.8268 - Val Acc: 73.91% | F1: 0.74
Epoch [08/15] | Train Loss: 0.3739 - Train Acc: 86.17% | Val Loss: 0.9253 - Val Acc: 71.91% | F1: 0.72
Epoch [09/15] | Train Loss: 0.3106 - Train Acc: 88.65% | Val Loss: 0.9567 - Val Acc: 71.04% | F1: 0.71
Epoch [10/15] | Train Loss: 0.2361 - Train Acc: 91.47% | Val Loss: 1.1738 - Val Acc: 66.79% | F1: 0.67
Epoch [11/15] | Train Loss: 0.2016 - Train Acc: 92.76% | Val Loss: 1.2010 - Val Acc: 70.54% | F1: 0.71
Epoch [12/15] | Train Loss: 0.1737 - Train Acc: 93.69% | Val Loss: 1.3363 - Val Acc: 71.79% | F1: 0.72
Epoch [13/15] | Train Loss: 0.1204 - Train Acc: 95.77% | Val Loss: 1.4063 - Val Acc: 71.41% | F1: 0.71
Epoch [14/15] | Train Loss: 0.0989 - Train Acc: 96.48% | Val Loss: 1.4222 - Val Acc: 70.16% | F1: 0.70
Epoch [15/15] | Train Loss: 0.0960 - Train Acc: 96.74% | Val Loss: 1.5962 - Val Acc: 69.79% | F1: 0.70
--------------------------------------------------
Training Complete!


=== GreenNet on orgs ===

 Starting Training Routine...
--------------------------------------------------
Epoch [01/15] | Train Loss: 0.3840 - Train Acc: 87.52% | Val Loss: 0.0895 - Val Acc: 97.33% | F1: 0.97
Epoch [02/15] | Train Loss: 0.1094 - Train Acc: 96.30% | Val Loss: 0.0683 - Val Acc: 98.24% | F1: 0.98
Epoch [03/15] | Train Loss: 0.0677 - Train Acc: 97.79% | Val Loss: 0.0530 - Val Acc: 98.63% | F1: 0.99
Epoch [04/15] | Train Loss: 0.0450 - Train Acc: 98.55% | Val Loss: 0.0476 - Val Acc: 98.70% | F1: 0.99
Epoch [05/15] | Train Loss: 0.0346 - Train Acc: 98.92% | Val Loss: 0.1031 - Val Acc: 98.31% | F1: 0.98
Epoch [06/15] | Train Loss: 0.0231 - Train Acc: 99.34% | Val Loss: 0.0759 - Val Acc: 98.76% | F1: 0.99
Epoch [07/15] | Train Loss: 0.0220 - Train Acc: 99.33% | Val Loss: 0.0655 - Val Acc: 99.15% | F1: 0.99
Epoch [08/15] | Train Loss: 0.0153 - Train Acc: 99.60% | Val Loss: 0.0886 - Val Acc: 97.85% | F1: 0.98
Epoch [09/15] | Train Loss: 0.0283 - Train Acc: 99.15% | Val Loss: 0.0973 - Val Acc: 97.66% | F1: 0.98
Epoch [10/15] | Train Loss: 0.0170 - Train Acc: 99.44% | Val Loss: 0.0408 - Val Acc: 99.28% | F1: 0.99
Epoch [11/15] | Train Loss: 0.0170 - Train Acc: 99.46% | Val Loss: 0.0597 - Val Acc: 98.83% | F1: 0.99
Epoch [12/15] | Train Loss: 0.0174 - Train Acc: 99.49% | Val Loss: 0.1170 - Val Acc: 98.37% | F1: 0.98
Epoch [13/15] | Train Loss: 0.0174 - Train Acc: 99.46% | Val Loss: 0.0771 - Val Acc: 98.37% | F1: 0.98
Epoch [14/15] | Train Loss: 0.0108 - Train Acc: 99.74% | Val Loss: 0.0550 - Val Acc: 99.48% | F1: 0.99
Epoch [15/15] | Train Loss: 0.0027 - Train Acc: 99.93% | Val Loss: 0.0981 - Val Acc: 98.96% | F1: 0.99
--------------------------------------------------
Training Complete!

==================================================
FINAL RESULTS SUMMARY
==================================================
AlexNet on cells | P: 0.9488 | R: 0.9488 | Val Acc: 94.88% | F1: 0.9488 | Time: 79.4 |Memory: 187.1MB | Latency: 0.216ms/sample
VGG16 on cells | P: 0.9598 | R: 0.9598 | Val Acc: 95.98% | F1: 0.9598 | Time: 281.2 |Memory: 632.9MB | Latency: 0.530ms/sample
ResNet18 on cells | P: 0.9839 | R: 0.9839 | Val Acc: 98.39% | F1: 0.9839 | Time: 471.5 |Memory: 791.0MB | Latency: 0.812ms/sample
GreenNet on cells | P: 0.9590 | R: 0.9590 | Val Acc: 95.90% | F1: 0.9590 | Time: 66.0 |Memory: 195.1MB | Latency: 0.223ms/sample
AlexNet on chest | P: 0.9675 | R: 0.9675 | Val Acc: 96.75% | F1: 0.9675 | Time: 29.7 |Memory: 183.0MB | Latency: 0.225ms/sample
VGG16 on chest | P: 0.9732 | R: 0.9732 | Val Acc: 97.32% | F1: 0.9732 | Time: 109.0 |Memory: 630.0MB | Latency: 0.543ms/sample
ResNet18 on chest | P: 0.9503 | R: 0.9503 | Val Acc: 95.03% | F1: 0.9503 | Time: 180.0 |Memory: 790.4MB | Latency: 0.802ms/sample
GreenNet on chest | P: 0.9809 | R: 0.9809 | Val Acc: 98.09% | F1: 0.9809 | Time: 23.0 |Memory: 194.2MB | Latency: 0.234ms/sample
AlexNet on lesions | P: 0.7316 | R: 0.7316 | Val Acc: 73.16% | F1: 0.7316 | Time: 48.1 |Memory: 185.8MB | Latency: 0.250ms/sample
VGG16 on lesions | P: 0.6891 | R: 0.6891 | Val Acc: 68.91% | F1: 0.6891 | Time: 169.2 |Memory: 632.0MB | Latency: 0.537ms/sample
ResNet18 on lesions | P: 0.7428 | R: 0.7428 | Val Acc: 74.28% | F1: 0.7428 | Time: 276.8 |Memory: 789.7MB | Latency: 0.823ms/sample
GreenNet on lesions | P: 0.6979 | R: 0.6979 | Val Acc: 69.79% | F1: 0.6979 | Time: 39.8 |Memory: 194.0MB | Latency: 0.224ms/sample
AlexNet on orgs | P: 0.9870 | R: 0.9870 | Val Acc: 98.70% | F1: 0.9870 | Time: 86.8 |Memory: 185.0MB | Latency: 0.229ms/sample
VGG16 on orgs | P: 0.9740 | R: 0.9740 | Val Acc: 97.40% | F1: 0.9740 | Time: 317.7 |Memory: 628.8MB | Latency: 0.531ms/sample
ResNet18 on orgs | P: 0.9915 | R: 0.9915 | Val Acc: 99.15% | F1: 0.9915 | Time: 525.5 |Memory: 787.9MB | Latency: 0.808ms/sample
GreenNet on orgs | P: 0.9896 | R: 0.9896 | Val Acc: 98.96% | F1: 0.9896 | Time: 67.6 |Memory: 193.7MB | Latency: 0.185ms/sample


------Training with just VGG---------------

==================================================
FINAL RESULTS SUMMARY
==================================================
GreenNet on cells | P: 0.9598 | R: 0.9598 | Val Acc: 95.98% | F1: 0.9598 | Time: 29.6 |Memory: 88.3MB | Latency: 0.051ms/sample
GreenNet on chest | P: 0.9675 | R: 0.9675 | Val Acc: 96.75% | F1: 0.9675 | Time: 8.7 |Memory: 87.0MB | Latency: 0.040ms/sample
GreenNet on lesions | P: 0.6966 | R: 0.6966 | Val Acc: 69.66% | F1: 0.6966 | Time: 16.1 |Memory: 88.3MB | Latency: 0.051ms/sample
GreenNet on orgs | P: 0.9883 | R: 0.9883 | Val Acc: 98.83% | F1: 0.9883 | Time: 25.4 |Memory: 87.1MB | Latency: 0.038ms/sample


----------------on testing got the following results:  

AlexNet on cells | P: 0.9635 | R: 0.9514 | Test Loss: 0.1363 | Test Acc: 95.97% | F1: 0.9563 | Time: 77.4s |Memory: 187.1MB | Latency: 0.268ms/sample
VGG16 on cells | P: 0.9078 | R: 0.8084 | Test Loss: 0.4771 | Test Acc: 83.02% | F1: 0.8268 | Time: 170.8s |Memory: 632.9MB | Latency: 0.385ms/sample
ResNet18 on cells | P: 0.9732 | R: 0.9739 | Test Loss: 0.0901 | Test Acc: 97.28% | F1: 0.9732 | Time: 245.1s |Memory: 791.0MB | Latency: 0.474ms/sample
GreenNet on cells | P: 0.9534 | R: 0.9460 | Test Loss: 0.2165 | Test Acc: 95.15% | F1: 0.9488 | Time: 63.2s |Memory: 195.1MB | Latency: 0.243ms/sample
AlexNet on chest | P: 0.8786 | R: 0.7329 | Test Loss: 1.0714 | Test Acc: 79.97% | F1: 0.7487 | Time: 23.1s |Memory: 183.0MB | Latency: 0.089ms/sample
VGG16 on chest | P: 0.8983 | R: 0.7957 | Test Loss: 0.8790 | Test Acc: 84.62% | F1: 0.8167 | Time: 54.2s |Memory: 630.0MB | Latency: 0.367ms/sample
ResNet18 on chest | P: 0.8900 | R: 0.7910 | Test Loss: 0.5403 | Test Acc: 84.13% | F1: 0.8113 | Time: 79.0s |Memory: 790.4MB | Latency: 0.341ms/sample
GreenNet on chest | P: 0.8791 | R: 0.7560 | Test Loss: 1.5506 | Test Acc: 81.57% | F1: 0.7744 | Time: 10.2s |Memory: 194.2MB | Latency: 0.077ms/sample
AlexNet on lesions | P: 0.4933 | R: 0.4274 | Test Loss: 0.6771 | Test Acc: 74.51% | F1: 0.4403 | Time: 25.4s |Memory: 185.8MB | Latency: 0.096ms/sample
VGG16 on lesions | P: 0.1449 | R: 0.1839 | Test Loss: 0.8550 | Test Acc: 68.33% | F1: 0.1620 | Time: 80.5s |Memory: 632.0MB | Latency: 0.260ms/sample
ResNet18 on lesions | P: 0.4306 | R: 0.4922 | Test Loss: 0.7571 | Test Acc: 71.62% | F1: 0.4557 | Time: 124.4s |Memory: 789.7MB | Latency: 0.345ms/sample
GreenNet on lesions | P: 0.5375 | R: 0.4613 | Test Loss: 1.5771 | Test Acc: 72.77% | F1: 0.4736 | Time: 21.5s |Memory: 194.0MB | Latency: 0.096ms/sample
AlexNet on orgs | P: 0.8906 | R: 0.8859 | Test Loss: 0.4025 | Test Acc: 89.97% | F1: 0.8861 | Time: 49.1s |Memory: 185.0MB | Latency: 0.069ms/sample
VGG16 on orgs | P: 0.8830 | R: 0.8710 | Test Loss: 0.3916 | Test Acc: 88.68% | F1: 0.8699 | Time: 147.3s |Memory: 628.8MB | Latency: 0.218ms/sample
ResNet18 on orgs | P: 0.8973 | R: 0.8905 | Test Loss: 0.3528 | Test Acc: 90.56% | F1: 0.8921 | Time: 248.4s |Memory: 787.9MB | Latency: 0.331ms/sample
GreenNet on orgs | P: 0.8827 | R: 0.8770 | Test Loss: 0.7809 | Test Acc: 88.95% | F1: 0.8766 | Time: 37.0s |Memory: 193.7MB | Latency: 0.067ms/sample










-------------------------Transfer Learning Part Training-----------------------------

Starting Training Routine...
--------------------------------------------------
Epoch [01/15] | Train Loss: 2.2805 - Train Acc: 23.33% | Val Loss: 2.1247 - Val Acc: 24.00% | Val Precision: 0.2136 - Val Recall: 0.1503 - Val F1: 0.1632
Epoch [02/15] | Train Loss: 1.6899 - Train Acc: 41.56% | Val Loss: 1.9998 - Val Acc: 34.00% | Val Precision: 0.2695 - Val Recall: 0.2121 - Val F1: 0.1975
Epoch [03/15] | Train Loss: 1.3372 - Train Acc: 58.44% | Val Loss: 1.7383 - Val Acc: 40.00% | Val Precision: 0.4078 - Val Recall: 0.3611 - Val F1: 0.3096
Epoch [04/15] | Train Loss: 1.1505 - Train Acc: 64.44% | Val Loss: 1.4358 - Val Acc: 56.00% | Val Precision: 0.5006 - Val Recall: 0.4949 - Val F1: 0.4741
Epoch [05/15] | Train Loss: 1.0271 - Train Acc: 71.56% | Val Loss: 1.3032 - Val Acc: 66.00% | Val Precision: 0.7197 - Val Recall: 0.6275 - Val F1: 0.6369
Epoch [06/15] | Train Loss: 0.8570 - Train Acc: 77.78% | Val Loss: 1.1966 - Val Acc: 70.00% | Val Precision: 0.7221 - Val Recall: 0.6439 - Val F1: 0.6070
Epoch [07/15] | Train Loss: 0.7965 - Train Acc: 76.67% | Val Loss: 1.1792 - Val Acc: 66.00% | Val Precision: 0.6756 - Val Recall: 0.6225 - Val F1: 0.5899
Epoch [08/15] | Train Loss: 0.7732 - Train Acc: 78.44% | Val Loss: 1.1259 - Val Acc: 64.00% | Val Precision: 0.6116 - Val Recall: 0.5631 - Val F1: 0.5483
Epoch [09/15] | Train Loss: 0.7485 - Train Acc: 80.22% | Val Loss: 1.0699 - Val Acc: 66.00% | Val Precision: 0.6405 - Val Recall: 0.6225 - Val F1: 0.5961
Epoch [10/15] | Train Loss: 0.6189 - Train Acc: 85.78% | Val Loss: 1.0798 - Val Acc: 66.00% | Val Precision: 0.6676 - Val Recall: 0.6427 - Val F1: 0.5961
Epoch [11/15] | Train Loss: 0.6106 - Train Acc: 84.44% | Val Loss: 1.0259 - Val Acc: 64.00% | Val Precision: 0.6576 - Val Recall: 0.5960 - Val F1: 0.5701
Epoch [12/15] | Train Loss: 0.6240 - Train Acc: 82.00% | Val Loss: 1.0166 - Val Acc: 72.00% | Val Precision: 0.7219 - Val Recall: 0.6755 - Val F1: 0.6658
Epoch [13/15] | Train Loss: 0.5097 - Train Acc: 88.44% | Val Loss: 0.9942 - Val Acc: 74.00% | Val Precision: 0.7235 - Val Recall: 0.7058 - Val F1: 0.6791
Epoch [14/15] | Train Loss: 0.5145 - Train Acc: 86.89% | Val Loss: 0.9872 - Val Acc: 74.00% | Val Precision: 0.7121 - Val Recall: 0.6730 - Val F1: 0.6579
Epoch [15/15] | Train Loss: 0.5173 - Train Acc: 87.33% | Val Loss: 1.0176 - Val Acc: 72.00% | Val Precision: 0.6813 - Val Recall: 0.6944 - Val F1: 0.6597
--------------------------------------------------
Training Complete!


Testing results:

Test Results
--------------------------------------------------
Test Loss: 1.7394
Test Accuracy: 49.50%
Test Precision: 0.5886
Test Recall: 0.4552
Test F1: 0.4677
