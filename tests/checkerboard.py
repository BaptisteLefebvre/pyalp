import pyalp as alp


# Allocate device
dev = alp.device.allocate_sequence_bis(verbose=True)

# Define protocol
pro = alp.protocol.Checkerboard()

# Display protocol
dev.display(pro)
