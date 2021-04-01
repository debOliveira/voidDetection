def compute_OF(img1,img2,pt0):
  # calculate optical flow
  p1, st, err = cv.calcOpticalFlowPyrLK(img1, img2, pt0, None, **lk_params)
  # calculate inverse optical flow
  p0r, _st, _err = cv.calcOpticalFlowPyrLK(img2, img1, p1, None, **lk_params)
  # validate optical flow to inverse flow
  d = abs(pt0-p0r).reshape(-1, 2).max(-1)
  good = d < 0.05
  # select good points
  good_new = p1[good==1]
  good_old = pt0[good==1]

  # create array of c and m coefficients of the lines (y = m*x + c)
  angle = []
  magnitude = []
  for i,(new,old) in enumerate(zip(good_new,good_old)):
    a,b = new.ravel()
    c,d = old.ravel()
    m = math.degrees(math.sqrt(pow(d-b,2)+pow(a-c,2)))
    a = math.degrees(math.atan2((b-d),(c-a)))
    if a < 0:
      a = a + 360
    angle.append(a)
    magnitude.append(m)
  return good_old,good_new,angle,magnitude