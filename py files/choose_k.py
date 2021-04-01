def choose_k(dataset,kmeans,n_clusters):
  mean_value = []
  # decision of k value of k neareast neighbors
  # stop criteria: 0.1% of previous estimated magnitudes
  for i in range(5, 100, 5):   
      knn = NearestNeighbors(n_neighbors=i) 
      knn.fit(dataset[:,0:2])
      idx = knn.kneighbors(kmeans.cluster_centers_[:,0:2].reshape(-1,2),
                          return_distance=False)
      m = np.array(np.mean(dataset[idx,3],axis=1))
      mean_value = np.append(mean_value,m,axis=0) 
      if i > 5:
        div = [i / j for i, j in zip(mean_value.reshape(-1, n_clusters)[-2,:] - m,
                                  mean_value.reshape(-1, n_clusters)[-2,:])]
        if div[np.argmax(np.array(div), axis=None)] < 0.1:
          n_neighbors = i
          break
  return n_neighbors