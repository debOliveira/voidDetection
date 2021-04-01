def feature_extraction(img1,img2):
  # initiate detector
  extractor = cv.xfeatures2d.SIFT_create(nOctaveLayers=3)
  # find the keypoints and descriptors
  kp1, des1 = extractor.detectAndCompute(img1,None)
  kp2, des2 = extractor.detectAndCompute(img2,None)  
  # create array of feature points in img1
  pt0 = [m.pt for m in kp1]
  pt0 = np.float32(pt0).reshape(-1,1,2)
  return pt0