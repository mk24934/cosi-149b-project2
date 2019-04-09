def moving_test_window_preds(n_future_preds):

    ''' n_future_preds - Represents the number of future predictions we want to make
                         This coincides with the number of windows that we will move forward
                         on the test data
    '''
    preds_moving = [] # Use this to store the prediction made on each test window
    moving_test_window = []
    moving_test_window.append(training_set_scaled[:column-5, :])       # Creating the first test window
    moving_test_window = np.array(moving_test_window)    # Making it an numpy array
    moving_test_window = np.reshape(moving_test_window, (moving_test_window.shape[0], moving_test_window.shape[1], 1))

    for i in range(n_future_preds):
        preds_one_step = regressor.predict(moving_test_window) # Note that this is already a scaled prediction so no need to rescale this
        preds_moving.append(preds_one_step[0,0]) # get the value from the numpy 2D array and append to predictions
        preds_one_step = preds_one_step.reshape(1,1,1) # Reshaping the prediction to 3D array for concatenation with moving test window
        moving_test_window = np.concatenate((moving_test_window[:,1:,:], preds_one_step), axis=1) # This is the new moving test window, where the first element from the window has been removed and the prediction  has been appended to the end
        print(moving_test_window)

    return preds_moving
