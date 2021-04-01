def clustering(X):
  n_clusters = choose_n(X)
  kmeans = KMeans(n_clusters = n_clusters, 
                  max_iter = 200).fit(X) 
  pred_y = kmeans.fit_predict(X) 
  return kmeans,pred_y,n_clusters