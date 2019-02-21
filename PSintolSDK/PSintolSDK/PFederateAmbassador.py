import copy
#HLA1516
#SintolRTOS data and modle callback interfae class
class P1516FederateAmbassador:
    def setSDKManager(self,value):
        self.sdkmng = value

    def synchronizationPointRegistrationSucceeded(self,label):
        print("synchronizationPointRegistrationSucceeded info:" + label + " ");

    def synchronizationPointRegistrationFailed(self,label,reason):
        print("synchronizationPointRegistrationFailed:" + label + " ");

    def announceSynchronizationPoint(self,label,theUserSuppliedTag):
        print("announceSynchronizationPoint:" + label + " ");
        self.sdkmng.synchronizationPointAchieved(label);

    def federationSynchronized(self,label):
        print("federationSynchronized:" + label + " ");
        self.sdkmng.insertSyncfedearetionSet(label);

    def initiateFederateSave(self,label):
        print("initiateFederateSave:" + label + " ");

    def initiateFederateSave(self,label,theTime):
         print("initiateFederateSave:" + label + " ");

    def federationSaved(self):
         print("federationSaved: ");

    def federationNotSaved(self,theSaveFailureReason):
        print("theSaveFailureReason:" + theSaveFailureReason + " ");

    def federationSaveStatusResponse(self,theFederateStatusVector):
         print("federationSaveStatusResponse: ");

    def requestFederationRestoreSucceeded(self,label):
        print("requestFederationRestoreSucceeded:" + label + " ");

    def requestFederationRestoreFailed(self,label):
        print("requestFederationRestoreFailed:" + label + " ");

    def federationRestoreBegun(self):
        print("federationRestoreBegun  ");

    def initiateFederateRestore(self,label,handle):
        print("initiateFederateRestore:" + label + " ");

    def federationRestored(self):
        print("federationRestored  ");

    def federationRestoreStatusResponse(self,theFederateStatusVector):
        print("federationRestoreStatusResponse  ");

    def startRegistrationForObjectClass(self,theClass):
        print("startRegistrationForObjectClass  ");

    def stopRegistrationForObjectClass(self,theClass):
        print("stopRegistrationForObjectClass  ");

    def turnInteractionsOn(self,theHandle):
        print("turnInteractionsOn  ");

    def turnInteractionsOff(self,theHandle):
        print("turnInteractionsOff  ");

    def objectInstanceNameReservationSucceeded(self,theObjectInstanceName):
        print("objectInstanceNameReservationSucceeded:" + theObjectInstanceName + "  ");

    def objectInstanceNameReservationFailed(self,theObjectInstanceName):
        print("objectInstanceNameReservationFailed:" + theObjectInstanceName + "  ");

    def objectInstanceNameReservationFailed(self,theObjectInstanceName):
        print("objectInstanceNameReservationFailed:" + theObjectInstanceName + "  ");

    def discoverObjectInstance(self,theObject,theObjectClass,theObjectInstanceName):
        print("discoverObjectInstance  ");

    def reflectAttributeValues(self,theObject,theAttributeValues,theUserSuppliedTag,sentOrder,theType):
        print("reflectAttributeValues  ");

    def reflectAttributeValues(self,theObject,theAttributeValues,theUserSuppliedTag,sentOrder,theType,theSentRegionHandleSet):
        print("reflectAttributeValues  ");

    def reflectAttributeValues(self,theObject,theAttributeValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder):
        print("reflectAttributeValues  ");

    def reflectAttributeValues(self,theObject,theAttributeValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder):
        print("reflectAttributeValues  ");

    def reflectAttributeValues(self,theObject,theAttributeValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder,theHandle):
        print("reflectAttributeValues  ");

    def reflectAttributeValues(self,theObject,theAttributeValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder,theHandle,theSentRegionHandleSet):
        print("reflectAttributeValues:%s" ,theAttributeValues.items());

    def receiveInteraction(self,theInteraction,theParameterValues,theUserSuppliedTag,sentOrder,theType):
        print("receiveInteraction  ");

    def receiveInteraction(self,theInteraction,theParameterValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder):
        print("receiveInteraction  ");

    def receiveInteraction(self,theInteraction,theParameterValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder,theSentRegionHandleSet):
        print("receiveInteraction  ");

    def receiveInteraction(self,theInteraction,theParameterValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder,theHandle):
        print("receiveInteraction  ");

    def receiveInteraction(self,theInteraction,theParameterValues,theUserSuppliedTag,sentOrder,theType,theTime,receivedOrder,theHandle,theSentRegionHandleSet):
        print("receiveInteraction  ");

    def removeObjectInstance(self,theObject,theUserSuppliedTag,sentOrder):
        print("removeObjectInstance  ");

    def removeObjectInstance(self,theObject,theUserSuppliedTag,sentOrder,theTime,receivedOrder):
        print("removeObjectInstance  ");

    def removeObjectInstance(self,theObject,theUserSuppliedTag,sentOrder,theTime,receivedOrder,theHandle):
        print("removeObjectInstance  ");

    def attributesInScope(self,theObject,theAttributes):
        print("attributesInScope  ");

    def attributesOutOfScope(self,theObject,theAttributes):
        print("attributesInScope  ");

    def provideAttributeValueUpdate(self,theObject,theAttributes,theUserSuppliedTag):
        print("attributesInScope  ");

    def turnUpdatesOnForObjectInstance(self,theObject,theAttributes):
        print("turnUpdatesOnForObjectInstance  ");

    def turnUpdatesOffForObjectInstance(self,theObject,theAttributes):
        print("turnUpdatesOffForObjectInstance  ");

    def requestAttributeOwnershipAssumption(self,theObject,offeredAttributes,theUserSuppliedTag):
        print("requestAttributeOwnershipAssumption  ");

    def requestDivestitureConfirmation(self,theObject,releasedAttributes):
        print("requestDivestitureConfirmation  ");

    def attributeOwnershipAcquisitionNotification(self,theObject,securedAttributes,theUserSuppliedTag):
        print("attributeOwnershipAcquisitionNotification  ");

    def attributeOwnershipUnavailable(self,theObject,theAttributes):
        print("attributeOwnershipUnavailable  ");

    def requestAttributeOwnershipRelease(self,theObject,candidateAttributes,theUserSuppliedTag):
        print("requestAttributeOwnershipRelease  ");

    def confirmAttributeOwnershipAcquisitionCancellation(self,theObject,theAttributes):
        print("confirmAttributeOwnershipAcquisitionCancellation  ");

    def informAttributeOwnership(self,theObject,theAttribute,theOwner):
        print("informAttributeOwnership  ");

    def attributeIsNotOwned(self,theObject,theAttribute):
        print("attributeIsNotOwned  ");

    def attributeIsOwnedByRTI(self,theObject,theAttribute):
        print("attributeIsOwnedByRTI  ");

    def timeRegulationEnabled(self,theObject,theAttribute):
        print("attributeIsOwnedByRTI  ");

    def timeConstrainedEnabled(self,theFederateTime):
        print("timeConstrainedEnabled  ");

    def timeAdvanceGrant(self,theTime):
        print("timeAdvanceGrant  ");

    def requestRetraction(self,theHandle):
        print("requestRetraction  ");

    def requestRetraction(self,theHandle):
        print("requestRetraction  ");