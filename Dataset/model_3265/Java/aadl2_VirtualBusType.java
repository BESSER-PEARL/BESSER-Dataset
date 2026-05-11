





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualBusType extends ComponentType, VirtualBusClassifier {






    private List<aadl2_DataPort> aadl2_dataports;




    private List<aadl2_EventDataPort> aadl2_eventdataports;




    private List<aadl2_EventPort> aadl2_eventports;


    public aadl2_VirtualBusType(
    ) {
        super(
        );
        this.aadl2_dataports = new ArrayList<>();
        this.aadl2_eventdataports = new ArrayList<>();
        this.aadl2_eventports = new ArrayList<>();
    }

    public aadl2_VirtualBusType(
        ArrayList<aadl2_DataPort> aadl2_dataports,        ArrayList<aadl2_EventDataPort> aadl2_eventdataports,        ArrayList<aadl2_EventPort> aadl2_eventports    ) {
        this.aadl2_dataports = aadl2_dataports;
        this.aadl2_eventdataports = aadl2_eventdataports;
        this.aadl2_eventports = aadl2_eventports;
    }


    public List<aadl2_DataPort> getAadl2_dataports() {
        return aadl2_dataports;
    }

    public void addAadl2_dataport(Aadl2_dataport aadl2_dataport) {
        this.aadl2_dataports.add(aadl2_dataport);
    }
    public List<aadl2_EventDataPort> getAadl2_eventdataports() {
        return aadl2_eventdataports;
    }

    public void addAadl2_eventdataport(Aadl2_eventdataport aadl2_eventdataport) {
        this.aadl2_eventdataports.add(aadl2_eventdataport);
    }
    public List<aadl2_EventPort> getAadl2_eventports() {
        return aadl2_eventports;
    }

    public void addAadl2_eventport(Aadl2_eventport aadl2_eventport) {
        this.aadl2_eventports.add(aadl2_eventport);
    }

}