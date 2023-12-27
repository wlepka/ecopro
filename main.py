import torch
import os
print("torch.cuda.is_available():", torch.cuda.is_available())
print("torch.cuda.device_count():", torch.cuda.device_count())
print("os.environ['CUDA_VISIBLE_DEVICES']:", os.environ.get('CUDA_VISIBLE_DEVICES'))


if torch.cuda.is_available():
    x = torch.cuda.FloatTensor(1)
    print("CUDA is available. GPU is working.")
else:
    print("CUDA is not available. No GPU detected.")
