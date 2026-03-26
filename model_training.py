import numpy as np

def load_images(file):
    with open(file, 'rb') as f:
        f.read(16)
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(-1, 28, 28)

def load_labels(file):
    with open(file, 'rb') as f:
        f.read(8)
        return np.frombuffer(f.read(), dtype=np.uint8)
from torchvision import datasets

emnist = datasets.EMNIST(
    root='./data',
    split='balanced',
    train=True,
    download=True
)
X = emnist.data.numpy()
y = emnist.targets.numpy()
print(X.shape, y.shape)