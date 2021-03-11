def reject_outliers(data,list1,list2,list3,m=1):
  mask = reject_outliers_mask(data,m)
  a = np.ma.compress_nd(np.ma.MaskedArray(list1, mask=~mask))
  b = np.ma.compress_nd(np.ma.MaskedArray(list2, mask=~mask))
  c = np.ma.compress_nd(np.ma.MaskedArray(list3, mask=~mask))
  return a,b,c