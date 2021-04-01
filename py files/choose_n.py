def choose_n(X):
  calinski = []
  davies = []
  # range of calinski + davies-bouldin test
  K = range(2, 16)
  for k in K:
      # Building and fitting the model
      kmeanModel = KMeans(n_clusters=k,random_state=1).fit(X)
      kmeanModel.fit(X)
      labels = kmeanModel.labels_ 
      # calculating index
      calinski.append(metrics.calinski_harabasz_score(X, labels))
      davies.append(metrics.davies_bouldin_score(X, labels))
  # get number of cluster for bigger calinski and lower davies-bouldin
  n_clusters = 2 + np.argmax(np.array([i / j for i, j in zip(calinski, davies)]),
                            axis=None)
  return n_clusters
