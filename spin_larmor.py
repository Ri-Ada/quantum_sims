import numpy as np

sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

omega = 1.0  
H = 0.5 * omega * sigma_z 
psi0 = np.array([1, 1], dtype=complex) / np.sqrt(2)