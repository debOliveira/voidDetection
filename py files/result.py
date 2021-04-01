def result(G_ab,kmeans,kmeans_cluster_centers_mag,of_idx,of_min_x,of_min_y,n_clusters,knn,dataset):
  dist = np.ones(n_clusters)*100
  valid = np.ones(n_clusters)
  for i in range(0,n_clusters): 
    # get pixel coordinates of VP point plane cantidate
    y_idx,x_idx = np.unravel_index(np.argmax(G_ab[:,:,i], axis=None),
                                    G_ab[:,:,i].shape)
    if (y_idx or x_idx): 
      # if vanishing point is not out of image
      x = int((x_idx+1.5)*side)
      y = int((y_idx+1.5)*side)
      dist[i] = math.hypot((int(of_min_y)-y), (int(of_min_x)-x))
    else: 
      valid[i] = 100

  # select nearest VP to OF cluster center
  nearest_VP = np.argmin(np.array(np.multiply(dist,valid)))
  # get pixel coordinates nearest VP to OF cluster center
  y_idx,x_idx = np.unravel_index(np.argmax(G_ab[:,:,nearest_VP], axis=None),
                                G_ab[:,:,nearest_VP].shape)
  x = int((x_idx+1.5)*side)
  y = int((y_idx+1.5)*side)
  for i in range(0,n_clusters): 
    # get distance of nearest VP to all cluster centers
    dist[i] = math.hypot((int(kmeans.cluster_centers_[i,1])-y), 
                        (int(kmeans.cluster_centers_[i,0])-x))
  # get magnitude for VP
  nearest_VP_mag_idx = knn.kneighbors(np.array(((x+of_min_x)/2,
                                                (y+of_min_y)/2)).reshape(-1,2), 
                                      return_distance=False)
  nearest_VP_mag = np.mean(dataset[nearest_VP_mag_idx.reshape(-1),3])
  if abs(kmeans_cluster_centers_mag[of_idx]-nearest_VP_mag) < 0.05*kmeans_cluster_centers_mag[of_idx]:
    print("VP valid")
  else:
    print("VP not valid")