def pre_VP_extracting(img2):
  cropped = img2[int(h/2):h,0:w]
  # gaussian filter for canny transformation processing
  blurred = cv.GaussianBlur(img2, (5, 5), 0)
  # canny edge filter
  edges = auto_canny(blurred,sigma=0.33)
  # line recognition via hough transform
  lines = cv.HoughLinesP(edges,rho = 1,theta = np.pi/180,
                        threshold = 100,minLineLength = 50,
                        maxLineGap = 10)
  return lines