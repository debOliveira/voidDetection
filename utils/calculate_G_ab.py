def calculate_G_ab(side,w,h,m_list,c_list,angle_list):  
  G_ab = np.zeros((int(h/side),int(w/side)))
  out = 0
  for idx,(a,b,theta) in enumerate(zip(m_list,c_list,angle_list)):
    for (c,d,gamma) in zip(m_list[(idx+1):len(m_list)],
                          c_list[(idx+1):len(m_list)],
                          angle_list[(idx+1):len(m_list)]):
      if abs(theta-gamma) < 10 and abs(theta-gamma) > 5 and a*c > 0:
        x = (d-b)/(a-c)
        y = a*x+b
        if x >= 0 and x < w and y >= 0 and y < h:
            G_ab[int(y/side),int(x/side)] = G_ab[int(y/side),int(x/side)] + 1
        else:
          out = out + 1
  return G_ab,out