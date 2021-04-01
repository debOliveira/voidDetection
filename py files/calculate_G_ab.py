def calculate_G_ab(side,w,h,m_list,c_list,angle_list):  
  G_ab = np.zeros((int(h/side),int(w/side)))
  for idx,(a,b,theta) in enumerate(zip(m_list,c_list,angle_list)):
    for (c,d,gamma) in zip(m_list[(idx+1):len(m_list)],
                          c_list[(idx+1):len(m_list)],
                          angle_list[(idx+1):len(m_list)]):
      if (theta>155):
        theta = theta-180     
      if abs(theta-gamma) < 15 and abs(theta-gamma) > 5: 
        x = (d-b)/(a-c)
        y = a*x+b
        if x >= 0 and x < w and y >= 0 and y < h:
            G_ab[int(y/side),int(x/side)] = G_ab[int(y/side),int(x/side)] + 1
  return G_ab