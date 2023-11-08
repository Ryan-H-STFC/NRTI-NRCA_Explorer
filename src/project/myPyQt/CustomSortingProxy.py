from __future__ import annotations
from PyQt5.QtCore import QModelIndex, QSortFilterProxyModel


class CustomSortingProxy(QSortFilterProxyModel):
    """
    Custom Sorting Proxy, allows the columns of the table to be sorted based on the type of its data.

    Args:
        QSortFilterProxyModel (Class): Parent Class which CustomSorting Proxy
    """

    def __init__(self):
        super(QSortFilterProxyModel, self).__init__()

    def lessThan(self, left: QModelIndex, right: QModelIndex) -> bool:
        """Custom Sorting Function, based on which type of data in each column of the table, adjust how the values will
         be sorted. Defaulting to the normal ``QSortFilterProxyModel.lessThan`` results. 

        Args:
            left (QModelIndex): Value on the left of the < operation
            right (QModelIndex): Value on the right of the < operation

        Returns:
            bool: Result of operation
        .. code-block:: text
            left.data() < right.data()
        """
        col = left.column()
        dataLeft = left.data()
        dataRight = right.data()

        match (col):
            case 0:
                # Rank of Integral (int)
                dataLeft = int(dataLeft)
                dataRight = int(dataRight)
                return dataLeft < dataRight

            case 2 | 6:
                # Rank of ... in format (123) (int)
                dataLeft = int(dataLeft[1:-1])
                dataRight = int(dataRight[1:-1])
                return dataLeft < dataRight
            case 1 | 3 | 4 | 5 | 7:
                # Numerical Data (float)
                dataLeft = float(dataLeft)
                dataRight = float(dataRight)
                return dataLeft < dataRight

        return super(QSortFilterProxyModel, self).lessThan(left, right)

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        # print(source_parent)
        # self.sourceModel().index(source_parent)
        # if source_parent

        return super().filterAcceptsRow(source_row, source_parent)