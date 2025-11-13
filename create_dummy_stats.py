#!/usr/bin/env python3
"""
Create dummy normalization statistics files for synthetic data testing.
Run this script to generate placeholder stat files that allow training with synthetic data.
"""

import numpy as np
import os

# Create stats directory if it doesn't exist
os.makedirs('stats', exist_ok=True)

# Number of channels in the dataset
n_channels = 73

print("Creating dummy normalization statistics files...")

# Create dummy files
# - mins/maxs: Use 0 and 1 for minmax normalization
# - means: Use 0 (no shift)
# - stds: Use 1 (no scaling)
np.save('stats/mins.npy', np.zeros(n_channels, dtype=np.float32))
np.save('stats/maxs.npy', np.ones(n_channels, dtype=np.float32))
np.save('stats/time_means.npy', np.zeros(n_channels, dtype=np.float32))
np.save('stats/global_means.npy', np.zeros(n_channels, dtype=np.float32))
np.save('stats/global_stds.npy', np.ones(n_channels, dtype=np.float32))
np.save('stats/time_diff_means.npy', np.zeros(n_channels, dtype=np.float32))
np.save('stats/time_diff_stds.npy', np.ones(n_channels, dtype=np.float32))

print(f"✓ Created 7 dummy stat files in ./stats/ for {n_channels} channels")
print("  - mins.npy, maxs.npy")
print("  - time_means.npy, global_means.npy, global_stds.npy")
print("  - time_diff_means.npy, time_diff_stds.npy")
print("\nThese files contain dummy values (0s and 1s) for testing with synthetic data.")
