import abc
import os
import random


class AbstractProxy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def delete(self, address):
        pass

    @abc.abstractmethod
    def count(self):
        pass


class LocalProxy(AbstractProxy):
    def __init__(self):
        super().__init__()
        self._address_set = []
        address_file = 'local_proxy.tmp'
        if os.path.exists(address_file):
            with open(address_file) as f:
                self._address_set = [x.replace('\n', '') for x in f if x]

    def get(self):
        return random.choice(self._address_set) if self._address_set else None

    def delete(self, address):
        if address in self._address_set:
            self._address_set.remove(address)

    def count(self):
        return len(self._address_set)
