# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 5,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# intrisics matrix/distortion
K = np.array([[858.33112278,   0.        , 946.93039627],
              [  0.        , 863.5177519 , 552.31426194],
              [  0.        ,   0.        ,   1.        ]])
D = np.array([[-0.24994682,  0.08369423, -0.00041109,  0.00032292, -0.0149    ]])

# image height and width
w = 1280
h = 720

#verbose flag
verbose = 1

