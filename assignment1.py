import matplotlib
from qiskit.visualization import plot_bloch_vector
from matplotlib import pyplot as plt

matplotlib.use("qtagg")

fig = plot_bloch_vector([0, -1, 0])

plt.show()
