def angular_filter(x_new_MagValid, y_new_MagValid, magnitude_MagValid, angle_MagValid):  
  # decision of sigma value of poisson sigma parameter 
  sigma = choose_sigma(angle_MagValid)
  # mask and angle poisson filtering
  mask = reject_outliers_mask(angle_MagValid,sigma)
  magnitudeValid = np.ma.compress_nd(np.ma.MaskedArray(magnitude_MagValid, 
                                                       mask=~mask))
  angleValid = np.ma.compress_nd(np.ma.MaskedArray(angle_MagValid, mask=~mask))
  xValid = np.ma.compress_nd(np.ma.MaskedArray(x_new_MagValid, mask=~mask))
  yValid = np.ma.compress_nd(np.ma.MaskedArray(y_new_MagValid, mask=~mask))
  return xValid,yValid,angleValid,magnitudeValid
