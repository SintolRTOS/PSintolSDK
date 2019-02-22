import sys
# sys.path.append('C:\\SintolRTOS\\PSintolSDK\\PSintolSDK\\PSintolSDK')
import CPSintolSDK as sintolsdk
from PFederateAmbassador import P1516FederateAmbassador
import threading
import time

class SintolSDKManager:
    
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(SintolSDKManager, "_instance"):
            with SintolSDKManager._instance_lock:
                if not hasattr(SintolSDKManager, "_instance"):
                    SintolSDKManager._instance = object.__new__(cls)  
        return SintolSDKManager._instance

    def __init__(self):
        self.isStarted = False
        self._synchronsized = 0
        self._federateSet = []

    def __del__(self):
        if self.isStarted == True:
            self.Stop()
     
    def Stop(self):
        try:
            self.ambassador.resignFederationExecution(sintolsdk.CANCEL_THEN_DELETE_THEN_DIVEST)
            self.ambassador.destroyFederationExecution(self._federateName)
            self._synchronsized = 0
            self.isStarted = False
        except Exception as e:
            print(e)
            return

    def InitSDK(self,federaambassador,
                federationExecutionName,
                federateType,
                fullPathNameToTheFDDfile,
                connectaddress,
                localtimefactory):
        self._federateName = federationExecutionName
        self._federateType = federateType
        self._federateSet = []
        self._federateSet.append(federateType)

        try:
            arg0 = 'protocol=rti'
            arg1 = 'address=' + connectaddress;
            self.ambassador = sintolsdk.RTIambassador(arg0,arg1)
            self.ambassador.createFederationExecution(federationExecutionName,fullPathNameToTheFDDfile,localtimefactory)
        except Exception as e:
            print(e)

        try:
            self.federateAmbassador = P1516FederateAmbassador()
            self.federateAmbassador.setSDKManager(self)
            self._federateHandle = self.ambassador.joinFederationExecution(self._federateType,self._federateName,self.federateAmbassador)
        except Exception as e:
            print(e)

        if self.waitForAllFederates() == False:
            return False

        self.isStarted = True

        if self.execJoined() == False:
            return False

        return True

    def Update(self,approximateMinimumTimeInSeconds):
        if self.isStarted == True:
            self.ambassador.evokeCallback(approximateMinimumTimeInSeconds)
    
    def execJoined(self):
        return True

    def waitForAllFederates(self):
        self._synchronized = 0
        try:
            self.ambassador.registerFederationSynchronizationPoint(self._federateType,"python".encode())
            self.ambassador.evokeCallback(10)
        except Exception as e:
            print(e)
            return False
        return True

    def insertSyncfedearetionSet(self,label):
        if self._federateSet.count(label) == 0:
            self._federateSet.append(label)
            return True
        return False

    def synchronizationPointAchieved(self,label):
        if self._federateSet.count(label) == 0:
            self.ambassador.synchronizationPointAchieved(label)

    def getObjectClassHandle(self,name):
        return self.ambassador.getObjectClassHandle(name)

    def getAttributeHandle(self,rti1516ObjectClassHandle,attributeName):
        return self.ambassador.getAttributeHandle(rti1516ObjectClassHandle,attributeName)

    def publishObjectClassAttributes(self,theClass,rti1516AttributeHandleSet):
        return self.ambassador.publishObjectClassAttributes(theClass,rti1516AttributeHandleSet)

    def subscribeObjectClassAttributes(self,theClass,attributeList,active):
        self.ambassador.subscribeObjectClassAttributes(theClass,attributeList,active)

    def registerObjectInstance(self,rti1516ObjectClassHandle):
        return self.ambassador.registerObjectInstance(rti1516ObjectClassHandle)

    def updateAttributeValues(self,rti1516ObjectInstanceHandle,rti1516AttributeValues,rti1516Tag):
        self.ambassador.updateAttributeValues(rti1516ObjectInstanceHandle,rti1516AttributeValues,rti1516Tag)

    def deleteObjectInstance(self,rti1516ObjectInstanceHandle,rti1516Tag):
        self.ambassador.deleteObjectInstance(rti1516ObjectInstanceHandle,rti1516Tag)

    def unpublishObjectClass(self,rti1516ObjectClassHandle):
        self.ambassador.unpublishObjectClass(rti1516ObjectClassHandle)

    def unpublishObjectClassAttributes(self,rti1516ObjectClassHandle,rti1516AttributeHandleSet):
        self.ambassador.unpublishObjectClassAttributes(rti1516ObjectClassHandle,rti1516AttributeHandleSet)

    def unsubscribeObjectClass(self,rti1516ObjectClassHandle):
        self.ambassador.unsubscribeObjectClass(rti1516ObjectClassHandle)

#Test SintolSDKManager
print('Start Test SintolSDKManager')
federaambassador = P1516FederateAmbassador()
sdkmng = SintolSDKManager()
federationExecutionName = 'UnrealRTOS'
federateType = 'Python'
fedfile = 'C:/SintolRTOS/UnrealRTOS/Binaries/Win64/multiAI.xml'
connectAddress = '192.168.86.163:14321'
hlatime  = 'HLAinteger64Time'
sdkmng.InitSDK(federaambassador,federationExecutionName,federateType,fedfile,connectAddress,hlatime)
_attributionset = [];
try:
    _characterObjHandle = sdkmng.getObjectClassHandle('MultiEntity')
    _characterAttributeHandle = sdkmng.getAttributeHandle(_characterObjHandle, 'playerAttribution')
    _attributionset.append(_characterAttributeHandle)

    sdkmng.publishObjectClassAttributes(_characterObjHandle,_attributionset)
    sdkmng.subscribeObjectClassAttributes(_characterObjHandle,_attributionset,True)
    _charactorObjInstance = sdkmng.registerObjectInstance(_characterObjHandle)

    while True:
        sdkmng.Update(0.01)
        time.sleep(0.01)

    sdkmng.deleteObjectInstance(_charactorObjInstance,'MultiAI_02')
    sdkmng.unsubscribeObjectClass(_characterObjHandle)

    sdkmng.Stop()
except Exception as e:
    print(e)




