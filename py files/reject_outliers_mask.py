def reject_outliers_mask(data, m=2):
    return abs(data - np.mean(data)) < m * np.std(data)