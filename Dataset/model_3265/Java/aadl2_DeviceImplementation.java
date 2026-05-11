





import java.util.List;
import java.util.ArrayList;

public class aadl2_DeviceImplementation extends ComponentImplementation, DeviceClassifier {






    private List<aadl2_BusSubcomponent> aadl2_bussubcomponents;




    private List<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents;




    private List<aadl2_DataSubcomponent> aadl2_datasubcomponents;


    public aadl2_DeviceImplementation(
    ) {
        super(
        );
        this.aadl2_bussubcomponents = new ArrayList<>();
        this.aadl2_virtualbussubcomponents = new ArrayList<>();
        this.aadl2_datasubcomponents = new ArrayList<>();
    }

    public aadl2_DeviceImplementation(
        ArrayList<aadl2_BusSubcomponent> aadl2_bussubcomponents,        ArrayList<aadl2_VirtualBusSubcomponent> aadl2_virtualbussubcomponents,        ArrayList<aadl2_DataSubcomponent> aadl2_datasubcomponents    ) {
        this.aadl2_bussubcomponents = aadl2_bussubcomponents;
        this.aadl2_virtualbussubcomponents = aadl2_virtualbussubcomponents;
        this.aadl2_datasubcomponents = aadl2_datasubcomponents;
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
    public List<aadl2_DataSubcomponent> getAadl2_datasubcomponents() {
        return aadl2_datasubcomponents;
    }

    public void addAadl2_datasubcomponent(Aadl2_datasubcomponent aadl2_datasubcomponent) {
        this.aadl2_datasubcomponents.add(aadl2_datasubcomponent);
    }

}