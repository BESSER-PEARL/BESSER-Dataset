





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualProcessorImplementation extends ComponentImplementation, VirtualProcessorClassifier {






    private List<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents;




    private List<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents;


    public aadl2_VirtualProcessorImplementation(
    ) {
        super(
        );
        this.aadl2_virtualbussubcomponents = new ArrayList<>();
        this.aadl2_virtualprocessorsubcomponents = new ArrayList<>();
    }

    public aadl2_VirtualProcessorImplementation(
        ArrayList<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents,        ArrayList<aadl2_VirtualProcessorSubcomponent> aadl2_virtualprocessorsubcomponents    ) {
        this.aadl2_virtualbussubcomponents = aadl2_virtualbussubcomponents;
        this.aadl2_virtualprocessorsubcomponents = aadl2_virtualprocessorsubcomponents;
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