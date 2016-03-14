from .neuron_pool import NeuronPool, PoolConfig


class Environment:
    neuron_pool = None

    def __init__(self):
        pool_config = PoolConfig()
        self.neuron_pool = NeuronPool()
        self.neuron_pool.construct(pool_config)

    def learn(self, epoch_count=10):
        success = False
        current_epoch = 0
        while not success and current_epoch <= epoch_count:
            input_neurons = self.neuron_pool.get_input()
            input_neurons[0].modify(0.5)

            out_neurons = self.neuron_pool.get_output()
            if out_neurons[0].is_active() and not out_neurons[1].is_active():
                success = True
            else:
                self.neuron_pool.process()

            current_epoch += 1

        return success
