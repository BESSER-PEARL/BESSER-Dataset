





import java.util.List;
import java.util.ArrayList;

public class aadl2_SystemImplementation extends ComponentImplementation, SystemClassifier {






    private List<aadl2_MemorySubcomponent> aadl2_memorysubcomponents;




    private List<aadl2_SubprogramGroupSubcomponent> aadl2_subprogramgroupsubcomponents;




    private List<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents;




    private List<aadl2_DeviceSubcomponent> aadl2_devicesubcomponents;




    private List<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents;




    private List<aadl2_ProcessSubcomponent> aadl2_processsubcomponents;




    private List<aadl2_SystemSubcomponent> aadl2_systemsubcomponents;




    private List<aadl2_BusSubcomponent> aadl2_bussubcomponents;




    private List<aadl2_ProcessorSubcomponent> aadl2_processorsubcomponents;




    private List<aadl2_DataSubcomponent> aadl2_datasubcomponents;




    private List<aadl2_SubprogramSubcomponent> aadl2_subprogramsubcomponents;


    public aadl2_SystemImplementation(
    ) {
        super(
        );
        this.aadl2_memorysubcomponents = new ArrayList<>();
        this.aadl2_subprogramgroupsubcomponents = new ArrayList<>();
        this.aadl2_virtualbussubcomponents = new ArrayList<>();
        this.aadl2_devicesubcomponents = new ArrayList<>();
        this.aadl2_virtualprocessorsubcomponents = new ArrayList<>();
        this.aadl2_processsubcomponents = new ArrayList<>();
        this.aadl2_systemsubcomponents = new ArrayList<>();
        this.aadl2_bussubcomponents = new ArrayList<>();
        this.aadl2_processorsubcomponents = new ArrayList<>();
        this.aadl2_datasubcomponents = new ArrayList<>();
        this.aadl2_subprogramsubcomponents = new ArrayList<>();
    }

    public aadl2_SystemImplementation(
        ArrayList<aadl2_MemorySubcomponent> aadl2_memorysubcomponents,        ArrayList<aadl2_SubprogramGroupSubcomponent> aadl2_subprogramgroupsubcomponents,        ArrayList<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents,        ArrayList<aadl2_DeviceSubcomponent> aadl2_devicesubcomponents,        ArrayList<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents,        ArrayList<aadl2_ProcessSubcomponent> aadl2_processsubcomponents,        ArrayList<aadl2_SystemSubcomponent> aadl2_systemsubcomponents,        ArrayList<aadl2_BusSubcomponent> aadl2_bussubcomponents,        ArrayList<aadl2_ProcessorSubcomponent> aadl2_processorsubcomponents,        ArrayList<aadl2_DataSubcomponent> aadl2_datasubcomponents,        ArrayList<aadl2_SubprogramSubcomponent> aadl2_subprogramsubcomponents    ) {
        this.aadl2_memorysubcomponents = aadl2_memorysubcomponents;
        this.aadl2_subprogramgroupsubcomponents = aadl2_subprogramgroupsubcomponents;
        this.aadl2_virtualbussubcomponents = aadl2_virtualbussubcomponents;
        this.aadl2_devicesubcomponents = aadl2_devicesubcomponents;
        this.aadl2_virtualprocessorsubcomponents = aadl2_virtualprocessorsubcomponents;
        this.aadl2_processsubcomponents = aadl2_processsubcomponents;
        this.aadl2_systemsubcomponents = aadl2_systemsubcomponents;
        this.aadl2_bussubcomponents = aadl2_bussubcomponents;
        this.aadl2_processorsubcomponents = aadl2_processorsubcomponents;
        this.aadl2_datasubcomponents = aadl2_datasubcomponents;
        this.aadl2_subprogramsubcomponents = aadl2_subprogramsubcomponents;
    }


    public List<aadl2_MemorySubcomponent> getAadl2_memorysubcomponents() {
        return aadl2_memorysubcomponents;
    }

    public void addAadl2_memorysubcomponent(Aadl2_memorysubcomponent aadl2_memorysubcomponent) {
        this.aadl2_memorysubcomponents.add(aadl2_memorysubcomponent);
    }
    public List<aadl2_SubprogramGroupSubcomponent> getAadl2_subprogramgroupsubcomponents() {
        return aadl2_subprogramgroupsubcomponents;
    }

    public void addAadl2_subprogramgroupsubcomponent(Aadl2_subprogramgroupsubcomponent aadl2_subprogramgroupsubcomponent) {
        this.aadl2_subprogramgroupsubcomponents.add(aadl2_subprogramgroupsubcomponent);
    }
    public List<aadl2_VirtualBusSubcomponent> getAadl2_virtualbussubcomponents() {
        return aadl2_virtualbussubcomponents;
    }

    public void addAadl2_virtualbussubcomponent(Aadl2_virtualbussubcomponent aadl2_virtualbussubcomponent) {
        this.aadl2_virtualbussubcomponents.add(aadl2_virtualbussubcomponent);
    }
    public List<aadl2_DeviceSubcomponent> getAadl2_devicesubcomponents() {
        return aadl2_devicesubcomponents;
    }

    public void addAadl2_devicesubcomponent(Aadl2_devicesubcomponent aadl2_devicesubcomponent) {
        this.aadl2_devicesubcomponents.add(aadl2_devicesubcomponent);
    }
    public List<aadl2_VirtualProcessorSubcomponent> getAadl2_virtualprocessorsubcomponents() {
        return aadl2_virtualprocessorsubcomponents;
    }

    public void addAadl2_virtualprocessorsubcomponent(Aadl2_virtualprocessorsubcomponent aadl2_virtualprocessorsubcomponent) {
        this.aadl2_virtualprocessorsubcomponents.add(aadl2_virtualprocessorsubcomponent);
    }
    public List<aadl2_ProcessSubcomponent> getAadl2_processsubcomponents() {
        return aadl2_processsubcomponents;
    }

    public void addAadl2_processsubcomponent(Aadl2_processsubcomponent aadl2_processsubcomponent) {
        this.aadl2_processsubcomponents.add(aadl2_processsubcomponent);
    }
    public List<aadl2_SystemSubcomponent> getAadl2_systemsubcomponents() {
        return aadl2_systemsubcomponents;
    }

    public void addAadl2_systemsubcomponent(Aadl2_systemsubcomponent aadl2_systemsubcomponent) {
        this.aadl2_systemsubcomponents.add(aadl2_systemsubcomponent);
    }
    public List<aadl2_BusSubcomponent> getAadl2_bussubcomponents() {
        return aadl2_bussubcomponents;
    }

    public void addAadl2_bussubcomponent(Aadl2_bussubcomponent aadl2_bussubcomponent) {
        this.aadl2_bussubcomponents.add(aadl2_bussubcomponent);
    }
    public List<aadl2_ProcessorSubcomponent> getAadl2_processorsubcomponents() {
        return aadl2_processorsubcomponents;
    }

    public void addAadl2_processorsubcomponent(Aadl2_processorsubcomponent aadl2_processorsubcomponent) {
        this.aadl2_processorsubcomponents.add(aadl2_processorsubcomponent);
    }
    public List<aadl2_DataSubcomponent> getAadl2_datasubcomponents() {
        return aadl2_datasubcomponents;
    }

    public void addAadl2_datasubcomponent(Aadl2_datasubcomponent aadl2_datasubcomponent) {
        this.aadl2_datasubcomponents.add(aadl2_datasubcomponent);
    }
    public List<aadl2_SubprogramSubcomponent> getAadl2_subprogramsubcomponents() {
        return aadl2_subprogramsubcomponents;
    }

    public void addAadl2_subprogramsubcomponent(Aadl2_subprogramsubcomponent aadl2_subprogramsubcomponent) {
        this.aadl2_subprogramsubcomponents.add(aadl2_subprogramsubcomponent);
    }

}