def main(img1_o,img2_o):

  ######################
  ### pre processing ###
  ######################
  # convert images to greyscale
  img1,img2 = img_reading(img1_o,img2_o)   
  # create array of feature points in img1
  pt0 = feature_extraction(img1,img2)
  
  ####################
  ### optical flow ###
  ####################
  # calculate optical flow
  good_old,good_new,angle,magnitude = compute_OF(img1,img2,pt0)  
  # remove the bigger 10% magnitude OF vectors
  x_new_MagValid,y_new_MagValid,magnitude_MagValid,angle_MagValid = magnitude_filter(angle,magnitude,good_old,good_new)
  # angle poisson filtering
  xValid,yValid,angleValid,magnitudeValid = angular_filter(x_new_MagValid, y_new_MagValid, magnitude_MagValid, angle_MagValid)  
  # identify if OF number filtered features is valid
  if len(xValid) > 100:
    print("OF identified")
  else:
    print("OF points NOT enough")
    breakpoint()  
  # creating datasets for unsupervisioned training
  dataset = np.array(list(zip(xValid, yValid,angleValid,
                              magnitudeValid))).reshape(len(xValid), 4)  
  # clustering
  kmeans,pred_y,n_clusters = clustering(dataset[:,0:3])
  # knn for clusters centers magnitude
  n_neighbors,kmeans_cluster_centers_mag,of_idx,of_min_x,of_min_y,knn = NN(dataset,kmeans,n_clusters)
  # identify if the drone is not in front of wall
  if abs(np.std(kmeans_cluster_centers_mag)) >= 500:
        print("Multiple planes available")
  else:
    print("Multiple planes NOT available")
    breakpoint()
  #####################
  ### VP extracting ###
  #####################
  # VP extracting Hough Lines
  lines = pre_VP_extracting(img2)
  # create n_clustered lists for m, c and angle of line
  for i in range(0,n_clusters):
    name = "list_"+str(i)
    globals()[name] = [0., 0., 0.]
  VP_extracting(lines,n_clusters,kmeans)
  # reorganize lists in 3 columns shape
  for i in range(0,n_clusters):
    name = "list_"+str(i)
    globals()[name] = np.array(globals()[name]).reshape(-1,3)
    globals()[name] = globals()[name][1:-1,:]
  G_ab = compute_Gab(n_clusters)
  result(G_ab,kmeans,kmeans_cluster_centers_mag,of_idx,of_min_x,of_min_y,n_clusters,knn,dataset)

