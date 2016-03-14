class Neuron:
    axons = []
    energy = 0
    activation_function = None

    def __init__(self, activation_function):
        self.activation_function = activation_function

    def set_akson(self, other_neuron, weight):
        self.axons.append((other_neuron, weight))

    def modify(self, amount):
        self.energy += amount

    def is_active(self):
        return self.activation_function(self.energy)

    def process(self):
        if self.is_active():
            for axon in self.axons:
                (neuron_to, weight) = axon
                neuron_to.modify(weight)

    def __str__(self):
        result = None
        for axon in self.axons:
            (neuron_to, weight) = axon
            result += weight + " "

        return result


