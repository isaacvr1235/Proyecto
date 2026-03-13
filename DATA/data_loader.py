from .dataset import Dataset, DatasetSplit

class DataLoader:
    def crear_dataset(self) -> Dataset:
        pass

class DataSplitter:
    def crear_split(self, dataset: Dataset) -> DatasetSplit:
        pass