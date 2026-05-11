





import java.util.List;
import java.util.ArrayList;

public class aadl2_SystemImplementation extends SystemClassifier, ComponentImplementation {






    private List<aadl2_ProcessorSubcomponent> aadl2_processorsubcomponents;




    private List<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents;




    private List<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents;




    private List<aadl2_SystemSubcomponent> aadl2_systemsubcomponents;


    public aadl2_SystemImplementation(
    ) {
        super(
        );
        this.aadl2_processorsubcomponents = new ArrayList<>();
        this.aadl2_virtualprocessorsubcomponents = new ArrayList<>();
        this.aadl2_virtualbussubcomponents = new ArrayList<>();
        this.aadl2_systemsubcomponents = new ArrayList<>();
    }

    public aadl2_SystemImplementation(
        ArrayList<aadl2_ProcessorSubcomponent> aadl2_processorsubcomponents,        ArrayList<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents,        ArrayList<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents,        ArrayList<aadl2_SystemSubcomponent> aadl2_systemsubcomponents    ) {
        this.aadl2_processorsubcomponents = aadl2_processorsubcomponents;
        this.aadl2_virtualprocessorsubcomponents = aadl2_virtualprocessorsubcomponents;
        this.aadl2_virtualbussubcomponents = aadl2_virtualbussubcomponents;
        this.aadl2_systemsubcomponents = aadl2_systemsubcomponents;
    }


    public List<aadl2_ProcessorSubcomponent> getAadl2_processorsubcomponents() {
        return aadl2_processorsubcomponents;
    }

    public void addAadl2_processorsubcomponent(Aadl2_processorsubcomponent aadl2_processorsubcomponent) {
        this.aadl2_processorsubcomponents.add(aadl2_processorsubcomponent);
    }
    public List<aadl2_VirtualProcessorSubcomponent> getAadl2_virtualprocessorsubcomponents() {
        return aadl2_virtualprocessorsubcomponents;
    }

    public void addAadl2_virtualprocessorsubcomponent(Aadl2_virtualprocessorsubcomponent aadl2_virtualprocessorsubcomponent) {
        this.aadl2_virtualprocessorsubcomponents.add(aadl2_virtualprocessorsubcomponent);
    }
    public List<aadl2_VirtualBusSubcomponent> getAadl2_virtualbussubcomponents() {
        return aadl2_virtualbussubcomponents;
    }

    public void addAadl2_virtualbussubcomponent(Aadl2_virtualbussubcomponent aadl2_virtualbussubcomponent) {
        this.aadl2_virtualbussubcomponents.add(aadl2_virtualbussubcomponent);
    }
    public List<aadl2_SystemSubcomponent> getAadl2_systemsubcomponents() {
        return aadl2_systemsubcomponents;
    }

    public void addAadl2_systemsubcomponent(Aadl2_systemsubcomponent aadl2_systemsubcomponent) {
        this.aadl2_systemsubcomponents.add(aadl2_systemsubcomponent);
    }

}