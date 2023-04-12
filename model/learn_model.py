# Load the pre-trained Yamnet model from TensorFlow Hub
loaded_yamnet = hub.load("https://tfhub.dev/google/yamnet/1")

# Create a Keras layer from the loaded model
yamnet_layer = hub.KerasLayer(loaded_yamnet, trainable=True) # put trainable into false if you don't want to train the weights

# Build a new model by adding the Yamnet layer and a new classification layer
num_classes = 10 # Change this to the number of classes in your new task
model = tf.keras.Sequential([yamnet_layer, tf.keras.layers.Dense(num_classes, activation='softmax')])

# Compile the model with a suitable optimizer, loss function, and evaluation metric
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])