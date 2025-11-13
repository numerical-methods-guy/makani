#!/usr/bin/env python3
"""
Create dummy normalization statistics files for synthetic data testing.
Run this script to generate placeholder stat files that allow training with synthetic data.
"""

import numpy as np
import os

# Create stats directory if it doesn't exist
os.makedirs('stats', exist_ok=True)

# Dataset dimensions
n_channels = 73
height = 721
width = 1440

print("Creating dummy normalization statistics files...")
print(f"  Shape: (1, {n_channels}, {height}, {width})")

# Create dummy files with proper 4D shape: (1, channels, height, width)
# - mins/maxs: Use 0 and 1 for minmax normalization
# - means: Use 0 (no shift)
# - stds: Use 1 (no scaling)
shape = (1, n_channels, height, width)

np.save('stats/mins.npy', np.zeros(shape, dtype=np.float32))
np.save('stats/maxs.npy', np.ones(shape, dtype=np.float32))
np.save('stats/time_means.npy', np.zeros(shape, dtype=np.float32))
np.save('stats/global_means.npy', np.zeros(shape, dtype=np.float32))
np.save('stats/global_stds.npy', np.ones(shape, dtype=np.float32))
np.save('stats/time_diff_means.npy', np.zeros(shape, dtype=np.float32))
np.save('stats/time_diff_stds.npy', np.ones(shape, dtype=np.float32))

print(f"✓ Created 7 dummy stat files in ./stats/")
print("  - mins.npy, maxs.npy")
print("  - time_means.npy, global_means.npy, global_stds.npy")
print("  - time_diff_means.npy, time_diff_stds.npy")
print("\nThese files contain dummy values (0s and 1s) for testing with synthetic data.")

# Calculate total file size
total_mb = 7 * shape[0] * shape[1] * shape[2] * shape[3] * 4 / (1024**2)  # 4 bytes per float32
print(f"Total size: ~{total_mb:.1f} MB")
