def VP_extracting(lines,n_clusters,kmeans):
  boundary = 40
  angle=[]
  # calculate, store and plot lines
  for idx,(x1,y1,x2,y2) in enumerate(lines.reshape(-1,4)):
      if x1 == x2: continue # pure horizontal lines
      elif y1 == y2: continue # pure vertical lines
      elif y1 < int(h/2) or y2 < int(h/2): continue # pure vertical lines
      else: 
        angle_l = math.degrees(math.atan2((y2-y1),(x2-x1)))
        if angle_l < 0:
          angle_l = angle_l + 360
          angle_wrap = angle_l - 180
        else:
          angle_wrap = angle_l
        if angle_wrap>boundary and angle_wrap<(180-boundary) and abs(angle_wrap-90)>10:
          A = np.vstack([(x1,x2),np.ones(len((x1,x2)))]).T
          m, c = np.linalg.lstsq(A, (y1,y2))[0]      
          x_y0 = int(-c/m)
          x_yh = int((h-c)/m)
          x_mean = (x1+x2)/2
          y_mean = (y1+y2)/2
          if lines.shape[0] > 100:
            x_diff = kmeans.cluster_centers_[:,0] - np.ones((1,n_clusters))*x_mean
            y_diff = kmeans.cluster_centers_[:,1] - np.ones((1,n_clusters))*y_mean
            r = np.sqrt(x_diff*x_diff + y_diff*y_diff)  
            idx = np.argmin(r, axis=None)
          else:
            idx = 0;
          name = "list_"+str(idx)
          n = [m,c,angle_wrap]
          globals()[name] = np.append(globals()[name],n,axis=0)
