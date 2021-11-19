''' Interfaces for DataAnalyse '''

from abc import ABC, abstractmethod


class DataAnalyseInterface(ABC):
    @abstractmethod
    def show_data():
        pass