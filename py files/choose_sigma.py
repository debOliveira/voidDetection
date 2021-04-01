def choose_sigma(angle_MagValid):
  # create vector to hold the number of filtered angles
  sum_mask = []
  # stop criteria: 0.05% of previous number of filtered vectors
  for i in range(1,10):
    mask = reject_outliers_mask(angle_MagValid,i)
    s = np.sum(mask)  
    sum_mask.append(s)
    if i > 1:
      if (s-sum_mask[-2]) < 0.05*sum_mask[-2]:
        sigma = i  
        break
  return sigma
