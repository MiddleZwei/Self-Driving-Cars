from keras.layers import Flatten, Convolution2D, Dense, Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from keras.losses import mean_squared_error

batch_size = 128


def save_model(model):
    import json
    import yaml

    model.save('model.h5')
    model.save_weights('weights.h5')

    json_model = model.to_json()
    yaml_model = model.to_yaml()

    with open('model.json', 'w') as outfile_json:
        json.dump(json_model, outfile_json)

    with open('model.yml', 'w') as outfile_yaml:
        yaml.dump(yaml_model, outfile_yaml, default_flow_style=False)


def cnn_model(batch_size=1,
              epochs=10,
              X_train=None,
              y_train=None,
              X_test=None,
              y_test=None):
    model = Sequential()

    model.add(Convolution2D(
        input_shape=(31, 98, 3),
        filters=24,
        kernel_size=(5, 5),
        strides=(2, 2),
        activation='relu'
    ))
    model.add(Convolution2D(
        input_shape=(14, 47, 3),
        filters=36,
        kernel_size=(5, 5),
        strides=(2, 2),
        activation='relu'
    ))
    model.add(Convolution2D(
        input_shape=(5, 22, 3),
        filters=48,
        kernel_size=(5, 5),
        strides=(2, 2),
        activation='relu'
    ))
    model.add(Convolution2D(
        input_shape=(3, 20, 3),
        filters=64,
        kernel_size=(3, 3),
        activation='relu'
    ))
    model.add(Convolution2D(
        input_shape=(1, 18, 3),
        filters=64,
        kernel_size=(3, 3),
        activation='relu'
    ))

    model.add(Flatten())

    model.add(Dropout(0.25))

    model.add(Dense(1164, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(10, activation='relu'))

    model.compile(loss=mean_squared_error,
                  optimizer=Adam(),
                  metrics=['accuracy'])

    model.compile(X_train, y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  verbose=1,
                  validation_data=(X_test, y_test))

    score = model.evaluate(X_test, y_test, verbose=1)

    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    save_model(model)
