import numpy
import torch

# Numpy
# To find the version of the Numpy installed in your system

print("Numpy Version is : " + numpy.__version__)

# PyTorch
# To find the version of the PyTorch installed in your system
# Latest version of the PyTorch can be downloaded via : https://pytorch.org/

print("Torch Version is : " + torch.__version__)

# CUDA
# Check if CUDA is availabe | To verify if the correct version of the PyTorch has been installed

print("Torch Version for CUDA available : ") 
print(torch.cuda.is_available())

print("Torch Example") 
x = torch.rand(5, 3)
print(x)
