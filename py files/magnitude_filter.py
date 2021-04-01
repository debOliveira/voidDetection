def magnitude_filter(angle,magnitude,good_old,good_new):
  # define number of itens to be eliminated
  k = int(len(magnitude)*0.1)
  # create array of ordered magnitude vectors
  idx = np.argpartition(magnitude,k)
  # mask to remove the bigger 10% magnitude OF vectors
  mask = np.ones_like(magnitude, dtype=bool)
  mask[idx[:k]] = False
  magnitude_MagValid = np.ma.compress_nd(np.ma.MaskedArray(magnitude, mask=~mask))
  x_new_MagValid = np.ma.compress_nd(np.ma.MaskedArray(good_new.reshape(-1,2)[:,0], 
                                                      mask=~mask))
  y_new_MagValid = np.ma.compress_nd(np.ma.MaskedArray(good_new.reshape(-1,2)[:,1], 
                                                      mask=~mask))
  angle_MagValid = np.ma.compress_nd(np.ma.MaskedArray(angle, mask=~mask))
  return x_new_MagValid, y_new_MagValid, magnitude_MagValid, angle_MagValid
