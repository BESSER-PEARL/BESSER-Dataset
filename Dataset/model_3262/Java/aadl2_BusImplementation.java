





import java.util.List;
import java.util.ArrayList;

public class aadl2_BusImplementation extends ComponentImplementation, BusClassifier {






    private List<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents;


    public aadl2_BusImplementation(
    ) {
        super(
        );
        this.aadl2_virtualbussubcomponents = new ArrayList<>();
    }

    public aadl2_BusImplementation(
        ArrayList<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents    ) {
        this.aadl2_virtualbussubcomponents = aadl2_virtualbussubcomponents;
    }


    public List<aadl2_VirtualBusSubcomponent> getAadl2_virtualbussubcomponents() {
        return aadl2_virtualbussubcomponents;
    }

    public void addAadl2_virtualbussubcomponent(Aadl2_virtualbussubcomponent aadl2_virtualbussubcomponent) {
        this.aadl2_virtualbussubcomponents.add(aadl2_virtualbussubcomponent);
    }

}