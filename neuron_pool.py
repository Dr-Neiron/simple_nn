from .neuron import Neuron


class PoolConfig:
    input_neuron_count = 2
    middle_neuron_count = 10
    out_neuron_count = 2

    @staticmethod
    def activation_function(energy):
        return energy >= 0.5


class NeuronPool:
    input_neurons = []
    middle_neurons = []
    out_neurons = []

    def __init__(self):
        pass

    def construct(self, construction_config):
        for i in range(0, construction_config.input_neuron_count - 1):
            neuron = Neuron(construction_config.activation_function)
            self.input_neurons.append(neuron)

        for i in range(0, construction_config.middle_neuron_count - 1):
            neuron = Neuron(construction_config.activation_function)
            self.middle_neurons.append(neuron)

        for i in range(0, construction_config.out_neuron_count - 1):
            neuron = Neuron(construction_config.activation_function)
            self.out_neurons.append(neuron)

        raise NotImplementedError('connect axons')

    def get_input(self):
        return self.input_neurons

    def get_output(self):
        return self.out_neurons

    def process(self):
        for neuron in self.input_neurons:
            neuron.process()
        for neuron in self.middle_neurons:
            neuron.process()
        for neuron in self.out_neurons:
            neuron.process()

    def dump(self):
        raise NotImplementedError


