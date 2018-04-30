import pyalp as alp



# Allocate device
dev = alp.device.allocate_sequence()

# Define protocol
pro = alp.protocol.BlackWhite(nb_repetitions=50)

# Display protocol
dev.display(pro)
