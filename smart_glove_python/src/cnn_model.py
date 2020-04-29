from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.layers import Conv2D, MaxPooling1D, ZeroPadding1D, Conv1D, ZeroPadding2D, MaxPooling2D
import tensorflow.keras.optimizers as opt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

import numpy as np
import pickle
import sys

def load_data(feature_path, label_path):
    with open(feature_path, 'rb') as f:
        feature = pickle.load(f)

    with open(label_path, 'rb') as f:
        label = pickle.load(f)

    return feature, label


def vgg_19(input_len):
    model = Sequential()
    model.add(ZeroPadding2D(padding=(1, 1), input_shape=(input_len[0], input_len[1], 1)))
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D((1, 2), strides=(2, 2)))

    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D((1, 2), strides=(2, 2)))

    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D((1, 2), strides=(2, 2)))

    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D((1, 2), strides=(2, 2)))

    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(ZeroPadding2D(padding=(1, 1)))
    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D((1, 2), strides=(2, 2)))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax'))

    return model

def vgg_19_1d(input_len):
    model = Sequential()
    model.add(ZeroPadding1D(padding=1, input_shape=(input_len[0], input_len[1])))
    model.add(Conv1D(32, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(32, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(1, strides=2))

    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(64, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(64, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(1, strides=2))

    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(128, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(128, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(128, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(128, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(1, strides=2))

    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(1, strides=2))

    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(ZeroPadding1D(padding=1))
    model.add(Conv1D(256, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(1, strides=2))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax'))

    return model


def encode_onehot(label, train_len):
    label = np.squeeze(label.reshape((1, -1)))

    label_encoder = LabelEncoder()
    encoded_label = label_encoder.fit_transform(label)
    encoded_label = encoded_label.reshape((-1, 1))

    train_label = encoded_label[:train_len, 0].reshape((-1, 1))
    test_label = encoded_label[train_len:, 0].reshape((-1, 1))

    onehot_encoder = OneHotEncoder()
    train_onehot = onehot_encoder.fit_transform(train_label)
    # print(encode_label.classes_)
    # print(encode_label.transform(label))

    return train_onehot, test_label


def encode_label(label):
    onehot_encoder = OneHotEncoder()
    onehot_label = onehot_encoder.fit_transform(label)
    # print(encode_label.classes_)
    # print(encode_label.transform(label))

    return onehot_label


if __name__ == "__main__":
    argument = sys.argv
    del argument[0]

    RESEARCH_QUESTION = argument[0]
    OS = argument[1]

    # RESEARCH_QUESTION = str('q1')
    # OS = 'unix'

    if(OS == str('unix')):
        TRAIN_FEATURE_PATH = './pickle/' + RESEARCH_QUESTION + '/train_feature_seq.pickle'
        TEST_FEATURE_PATH = './pickle/' + RESEARCH_QUESTION + '/test_feature_seq.pickle'

        TRAIN_LABEL_PATH = './pickle/' + RESEARCH_QUESTION + '/train_label_seq.pickle'
        TEST_LABEL_PATH = './pickle/' + RESEARCH_QUESTION + '/test_label_seq.pickle'

    if (OS == str('windows')):
        TRAIN_FEATURE_PATH = './pickle/' + RESEARCH_QUESTION + '/train_feature_seq.pickle'
        TEST_FEATURE_PATH = './pickle/' + RESEARCH_QUESTION + '/test_feature_seq.pickle'

        TRAIN_LABEL_PATH = './pickle/' + RESEARCH_QUESTION + '/train_label_seq.pickle'
        TEST_LABEL_PATH = './pickle/' + RESEARCH_QUESTION + '/test_label_seq.pickle'

    train_feature, train_label = load_data(TRAIN_FEATURE_PATH, TRAIN_LABEL_PATH)
    train_feature_ = train_feature.reshape((train_feature.shape[2], train_feature.shape[0], train_feature.shape[1], 1))

    test_feature, test_label = load_data(TEST_FEATURE_PATH, TEST_LABEL_PATH)
    test_feature_ = test_feature.reshape((test_feature.shape[2], test_feature.shape[0], train_feature.shape[1], 1))

    train_len = train_label.shape[0]
    test_len = test_label.shape[0]

    all_label = np.concatenate((train_label, test_label))

    train_onehot, test_labels = encode_onehot(all_label, train_len)

    # Test pretrained model
    model = vgg_19(train_feature.shape)

    # Optimizers
    sgd = opt.SGD(lr=0.006, momentum=0.5, nesterov=False)
    adam = opt.Adam(lr=0.03, beta_1=0.9, beta_2=0.999, amsgrad=False)
    rms_prop = opt.RMSprop(lr=0.01, rho=0.9)
    adagrad = opt.Adagrad(lr=0.01)
    adadelta = opt.Adadelta(lr=1.0, rho=0.95)
    adamax = opt.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999)
    nadam = opt.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999)

    model.compile(optimizer=adam, loss='categorical_crossentropy')

    print(model.summary())

    model.fit(train_feature_, train_onehot.toarray(),
                batch_size=32,
                # batch_size=1775,
                epochs=30
            )

    predicted_label = np.argmax(model.predict(test_feature_), axis=1).reshape((-1, 1))

    err_array = np.subtract(predicted_label, test_labels)
    err_idx = np.where(err_array != 0)[1]

    err = round(((len(err_idx) / test_len) * 100), 2)
    acc = 100 - err

    print('CNN model\'s accuracy is ', acc, '%')