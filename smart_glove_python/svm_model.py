from sklearn.svm import LinearSVC
import pickle
import numpy as np
from scipy.sparse import csr_matrix

def load_data(feature_path, label_path):
    with open(feature_path, 'rb') as f:
        feature = pickle.load(f)

    with open(label_path, 'rb') as f:
        label = pickle.load(f)

    return feature, label

if __name__ == '__main__':
    TRAIN_FEATURE_PATH = './pickle_files/train_feature_svm.pickle'
    TEST_FEATURE_PATH = './pickle_files/test_feature_svm.pickle'

    TRAIN_LABEL_PATH = './pickle_files/train_label_svm.pickle'
    TEST_LABEL_PATH = './pickle_files/test_label_svm.pickle'

    train_feature, train_label = load_data(TRAIN_FEATURE_PATH, TRAIN_LABEL_PATH)
    test_feature, test_label = load_data(TEST_FEATURE_PATH, TEST_LABEL_PATH)

    svm_model = LinearSVC(tol=1e-5)
    svm_model.fit(train_feature, np.squeeze(train_label))

    predicted_label = svm_model.predict(test_feature).reshape((-1, 1))
    test_len = len(predicted_label)

    err_array = np.subtract(predicted_label, test_label)
    err_idx = np.where(err_array != 0)[1]

    err = round(((len(err_idx)/ test_len) * 100), 2)
    acc = 100 - err

    print('SVM model accuracy: ', acc, '%')