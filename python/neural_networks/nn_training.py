import tensorflow as tf


loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

optimizer = tf.keras.optimizers.Adam()

train_loss = tf.keras.metrics.Mean(name="train_loss")
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")

test_loss = tf.keras.metrics.Mean(name="test_loss")
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="test_accuracy")


class NNTraining:
    def __init__(
        self,
        model: tf.keras.Model,
        optimizer: tf.keras.optimizers = tf.keras.optimizers.Adam,
        epochs: int = 256,
    ) -> None:
        self.model = model
        self.optimizer = optimizer
        self.epochs = epochs

    @tf.function
    def train_step(self, data: tf.Tensor, labels: tf.Tensor):
        with tf.GradientTape() as tape:
            # training=True is only needed if there are layers with different
            # behavior during training versus inference (e.g. Dropout).
            breakpoint()
            predictions = self.model(data, training=True)
            loss = loss_object(labels, predictions)
        gradients = tape.gradient(loss, self.model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))

        train_loss(loss)
        train_accuracy(labels, predictions)

    @tf.function
    def test_step(self, data: tf.Tensor, labels: tf.Tensor):
        # training=False is only needed if there are layers with different
        # behavior during training versus inference (e.g. Dropout).
        predictions = self.model(data, training=False)
        t_loss = loss_object(labels, predictions)

        test_loss(t_loss)
        test_accuracy(labels, predictions)

    def train_model(self, training_data, training_labels) -> None:
        for epoch in range(self.epochs):
            # Reset the metrics at the start of the next epoch
            train_loss.reset_states()
            train_accuracy.reset_states()
            test_loss.reset_states()
            test_accuracy.reset_states()

            # for training_data, training_labels in zip(training_data, training_labels):
            self.train_step(training_data, training_labels)

            # for test_images, test_labels in test_ds:
            #     test_step(test_images, test_labels)

            print(
                f"Epoch {epoch + 1}, "
                f"Loss: {train_loss.result()}, "
                f"Accuracy: {train_accuracy.result() * 100}, "
                f"Test Loss: {test_loss.result()}, "
                f"Test Accuracy: {test_accuracy.result() * 100}"
            )