class Operation:
    """ Represents a graph node that performs a computation

    An `Operation` is a node in a `Graph` that takes zero or more
    objects as input and returns zero or more objects as output.
    """

    def __init__(self, input_nodes=[]):
        """ Construct Operation
        """
        self.input_nodes = input_nodes

        # Initialize a set of consumers
        self.consumers = []

        # Append this node to the list of consumers of all inputs
        for input_node in input_nodes:
            input_node.consumers.append(self)

        # Append this operation to the list of ops in the currently active 
        # default graph
        _default_graph.operations.append(self)

    def compute(self):
        """ Computes the output of this operation
        Must be implemented by the particular operation
        """
        pass
