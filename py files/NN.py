def NN(dataset,kmeans,n_clusters):
  n_neighbors = choose_k(dataset,kmeans,n_clusters)
  # fit nearest neighbors for each cluster center for optimal k
  knn = NearestNeighbors(n_neighbors=n_neighbors)
  knn.fit(dataset[:,0:2])
  kmeans_cluster_centers_mag = np.zeros((n_clusters,1))
  for i in range(0,n_clusters):
    idx = knn.kneighbors(kmeans.cluster_centers_[i,0:2].reshape(-1,2), return_distance=False)
    kmeans_cluster_centers_mag[i] = np.mean(dataset[idx.reshape(-1),3])
  
  # getting center of lowest magnitude (furtherst plane)
  of_idx = np.argmin(kmeans_cluster_centers_mag, axis=None)
  of_min_x = kmeans.cluster_centers_[of_idx,0]
  of_min_y = kmeans.cluster_centers_[of_idx,1]

  return n_neighbors,kmeans_cluster_centers_mag,of_idx,of_min_x,of_min_y,knn
