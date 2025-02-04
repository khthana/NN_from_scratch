import numpy as np
import spiral

class Layer_Dense :

    def __init__ ( self , n_inputs , n_neurons ):
        # Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1 , n_neurons))
       
    # Forward pass
    def forward ( self , inputs ):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

x, y = spiral.create_data(samples=100, classes=3)

# Create Dense layer with 2 input features and 3 output values
dense1 = Layer_Dense( 2 , 3 )

# Perform a forward pass of our training data through this layer
dense1.forward(x)

# Let's see output of the first few samples:
print (dense1.output[: 5 ])