def compute_Gab(n_clusters): 
  # initialize variables
  G_ab = np.zeros((int(h/side),int(w/side),n_clusters))

  # compute greatest intersection point
  for i in range(0,n_clusters):
    name = "list_"+str(i)
    G_ab[:,:,i] = calculate_G_ab(side,w,h,
                                globals()[name][:,0],globals()[name][:,1],
                                globals()[name][:,2])
  return G_ab