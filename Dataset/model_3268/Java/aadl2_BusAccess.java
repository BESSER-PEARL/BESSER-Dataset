





import java.util.List;
import java.util.ArrayList;

public class aadl2_BusAccess extends Access {

    private String virtual;





    private aadl2_VirtualProcessorType aadl2_virtualprocessortype;




    private aadl2_DeviceType aadl2_devicetype;




    private aadl2_BusFeatureClassifier aadl2_busfeatureclassifier;




    private aadl2_MemoryType aadl2_memorytype;




    private aadl2_SystemType aadl2_systemtype;




    private aadl2_BusType aadl2_bustype;




    private aadl2_VirtualBusType aadl2_virtualbustype;




    private aadl2_FeatureGroupType aadl2_featuregrouptype;




    private aadl2_ProcessorType aadl2_processortype;




    private aadl2_AbstractType aadl2_abstracttype;


    public aadl2_BusAccess(
        String virtual    ) {
        super(
        );
        this.virtual = virtual;
    }


    public String getVirtual() {
        return virtual;
    }

    public void setVirtual(String virtual) {
        this.virtual = virtual;
    }

    public aadl2_VirtualProcessorType getAadl2_virtualprocessortype() {
        return aadl2_virtualprocessortype;
    }

    public void setAadl2_virtualprocessortype(aadl2_VirtualProcessorType aadl2_virtualprocessortype) {
        this.aadl2_virtualprocessortype = aadl2_virtualprocessortype;
    }
    public aadl2_DeviceType getAadl2_devicetype() {
        return aadl2_devicetype;
    }

    public void setAadl2_devicetype(aadl2_DeviceType aadl2_devicetype) {
        this.aadl2_devicetype = aadl2_devicetype;
    }
    public aadl2_BusFeatureClassifier getAadl2_busfeatureclassifier() {
        return aadl2_busfeatureclassifier;
    }

    public void setAadl2_busfeatureclassifier(aadl2_BusFeatureClassifier aadl2_busfeatureclassifier) {
        this.aadl2_busfeatureclassifier = aadl2_busfeatureclassifier;
    }
    public aadl2_MemoryType getAadl2_memorytype() {
        return aadl2_memorytype;
    }

    public void setAadl2_memorytype(aadl2_MemoryType aadl2_memorytype) {
        this.aadl2_memorytype = aadl2_memorytype;
    }
    public aadl2_SystemType getAadl2_systemtype() {
        return aadl2_systemtype;
    }

    public void setAadl2_systemtype(aadl2_SystemType aadl2_systemtype) {
        this.aadl2_systemtype = aadl2_systemtype;
    }
    public aadl2_BusType getAadl2_bustype() {
        return aadl2_bustype;
    }

    public void setAadl2_bustype(aadl2_BusType aadl2_bustype) {
        this.aadl2_bustype = aadl2_bustype;
    }
    public aadl2_VirtualBusType getAadl2_virtualbustype() {
        return aadl2_virtualbustype;
    }

    public void setAadl2_virtualbustype(aadl2_VirtualBusType aadl2_virtualbustype) {
        this.aadl2_virtualbustype = aadl2_virtualbustype;
    }
    public aadl2_FeatureGroupType getAadl2_featuregrouptype() {
        return aadl2_featuregrouptype;
    }

    public void setAadl2_featuregrouptype(aadl2_FeatureGroupType aadl2_featuregrouptype) {
        this.aadl2_featuregrouptype = aadl2_featuregrouptype;
    }
    public aadl2_ProcessorType getAadl2_processortype() {
        return aadl2_processortype;
    }

    public void setAadl2_processortype(aadl2_ProcessorType aadl2_processortype) {
        this.aadl2_processortype = aadl2_processortype;
    }
    public aadl2_AbstractType getAadl2_abstracttype() {
        return aadl2_abstracttype;
    }

    public void setAadl2_abstracttype(aadl2_AbstractType aadl2_abstracttype) {
        this.aadl2_abstracttype = aadl2_abstracttype;
    }

}