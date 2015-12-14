'''
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
"""
OpenCMISS-Neon Region Editor Widget

Displays and allows editing of the the Neon region tree.
"""

from PySide import QtCore, QtGui

from opencmiss.neon.core.neonregion import NeonRegion
from opencmiss.neon.ui.editors.ui_regioneditorwidget import Ui_RegionEditorWidget

class RegionTreeItem(object):

    def __init__(self, region, row, parent=None):
        self._region = region
        self._row = row
        self._parent = parent
        self._children = []
        childCount = region.getChildCount()
        for childRow in range(childCount):
            childRegion = region.getChild(childRow)
            childItem = RegionTreeItem(childRegion, childRow, self)
            self._children.append(childItem)

    def getRegion(self):
        return self._region

    def getRow(self):
        return self._row

    def getParent(self):
        return self._parent

    def getChild(self, i):
        if i < len(self._children):
            return self._children[i]
        return None

    def getChildCount(self):
        return len(self._children)

    def setInvisibleRootChild(self, rootItem):
        self._children = [rootItem]

class RegionTreeModel(QtCore.QAbstractItemModel):

    def __init__(self, rootRegion, parent):
        QtCore.QAbstractItemModel.__init__(self, parent)
        self._rootRegion = rootRegion
        dummyRegion = NeonRegion(None, None, None)
        self._invisibleRootItem = RegionTreeItem(dummyRegion, 0)
        if rootRegion is not None:
            rootItem = RegionTreeItem(rootRegion, 0, self._invisibleRootItem)
            self._invisibleRootItem.setInvisibleRootChild(rootItem)

    def setRootRegion(self, rootRegion):
        rootItem = RegionTreeItem(rootRegion, 0)
        self._invisibleRootItem.setInvisibleRootChild(rootItem)

    def columnCount(self, parentIndex):
        return 1

    def flags(self, index):
        if not index.isValid():
            return 0
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    #def headerData(self, section, orientation, role):
    #    if (orientation == QtCore.Qt.Horizontal) and (role == QtCore.Qt.DisplayRole) and (section == 0):
    #         return 'Name'
    #    return None

    def index(self, row, column, parentIndex):
        if not self.hasIndex(row, column, parentIndex):
            return QtCore.QModelIndex()
        if parentIndex.isValid():
            parentItem = parentIndex.internalPointer()
        else:
            parentItem = self._invisibleRootItem
        childItem = parentItem.getChild(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QtCore.QModelIndex()

    def rowCount(self, parentIndex):
        if parentIndex.column() > 0:
            return 0
        if parentIndex.isValid():
            parentItem = parentIndex.internalPointer()
        else:
            parentItem = self._invisibleRootItem
        return parentItem.getChildCount()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()
        item = index.internalPointer()
        parentItem = item.getParent()
        if parentItem and (parentItem is not self._invisibleRootItem):
            return self.createIndex(parentItem.getRow(), 0, parentItem)
        return QtCore.QModelIndex()

    def data(self, index, role):
        if not index.isValid():
            return None
        item = index.internalPointer()
        if (role == QtCore.Qt.DisplayRole) and (index.column() == 0):
            region = item.getRegion()
            regionName = region.getName()
            if regionName:
                return regionName
            else:
                return "/"
        return None

    def getRegionAtIndex(self, index):
        if not index.isValid():
            return None
        item = index.internalPointer()
        return item.getRegion()

class RegionEditorWidget(QtGui.QWidget):

    regionSelected = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._rootRegion = None
        self._regionItems = None
        # Using composition to include the visual element of the GUI.
        self._ui = Ui_RegionEditorWidget()
        self._ui.setupUi(self)
        self._makeConnections()

    def _makeConnections(self):
        self._ui.treeViewRegion.clicked.connect(self._regionTreeItemClicked)

    def setRootRegion(self, rootRegion):
        '''
        :param rootRegion: The root NeonRegion
        '''
        self._rootRegion = rootRegion
        # rebuild tree
        self._buildTree()

    def _buildTree(self):
        self._regionItems = RegionTreeModel(self._rootRegion, None)
        self._ui.treeViewRegion.setModel(self._regionItems)
        self._ui.treeViewRegion.header().hide()
        self._ui.treeViewRegion.expandAll()
        #if selectedIndex:
        #    self._ui.treeViewRegion.setCurrentIndex(selectedIndex)
        self._ui.treeViewRegion.show()

    def _regionTreeItemClicked(self, index):
        '''
        Calls back clients with newly selected region
        '''
        model = index.model()
        region = model.getRegionAtIndex(index)
        # regionPath = region.getPath()
        # print("Clicked on region " + regionPath)
        self.regionSelected.emit(region)