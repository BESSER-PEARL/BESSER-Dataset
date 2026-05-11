





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessorImplementation extends ProcessorClassifier, ComponentImplementation {






    private List<aadl2_MemorySubcomponent> aadl2_memorysubcomponents;




    private List<aadl2_BusSubcomponent> aadl2_bussubcomponents;




    private List<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents;




    private List<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents;


    public aadl2_ProcessorImplementation(
    ) {
        super(
        );
        this.aadl2_memorysubcomponents = new ArrayList<>();
        this.aadl2_bussubcomponents = new ArrayList<>();
        this.aadl2_virtualbussubcomponents = new ArrayList<>();
        this.aadl2_virtualprocessorsubcomponents = new ArrayList<>();
    }

    public aadl2_ProcessorImplementation(
        ArrayList<aadl2_MemorySubcomponent> aadl2_memorysubcomponents,        ArrayList<aadl2_BusSubcomponent> aadl2_bussubcomponents,        ArrayList<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents,        ArrayList<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents    ) {
        this.aadl2_memorysubcomponents = aadl2_memorysubcomponents;
        this.aadl2_bussubcomponents = aadl2_bussubcomponents;
        this.aadl2_virtualbussubcomponents = aadl2_virtualbussubcomponents;
        this.aadl2_virtualprocessorsubcomponents = aadl2_virtualprocessorsubcomponents;
    }


    public List<aadl2_MemorySubcomponent> getAadl2_memorysubcomponents() {
        return aadl2_memorysubcomponents;
    }

    public void addAadl2_memorysubcomponent(Aadl2_memorysubcomponent aadl2_memorysubcomponent) {
        this.aadl2_memorysubcomponents.add(aadl2_memorysubcomponent);
    }
    public List<aadl2_BusSubcomponent> getAadl2_bussubcomponents() {
        return aadl2_bussubcomponents;
    }

    public void addAadl2_bussubcomponent(Aadl2_bussubcomponent aadl2_bussubcomponent) {
        this.aadl2_bussubcomponents.add(aadl2_bussubcomponent);
    }
    public List<aadl2_VirtualBusSubcomponent> getAadl2_virtualbussubcomponents() {
        return aadl2_virtualbussubcomponents;
    }

    public void addAadl2_virtualbussubcomponent(Aadl2_virtualbussubcomponent aadl2_virtualbussubcomponent) {
        this.aadl2_virtualbussubcomponents.add(aadl2_virtualbussubcomponent);
    }
    public List<aadl2_VirtualProcessorSubcomponent> getAadl2_virtualprocessorsubcomponents() {
        return aadl2_virtualprocessorsubcomponents;
    }

    public void addAadl2_virtualprocessorsubcomponent(Aadl2_virtualprocessorsubcomponent aadl2_virtualprocessorsubcomponent) {
        this.aadl2_virtualprocessorsubcomponents.add(aadl2_virtualprocessorsubcomponent);
    }

}