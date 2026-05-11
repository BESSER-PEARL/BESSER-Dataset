





import java.util.List;
import java.util.ArrayList;

public class aadl2_MemoryType extends MemoryClassifier, ComponentType {






    private List<aadl2_DataPort> aadl2_dataports;




    private List<aadl2_EventDataPort> aadl2_eventdataports;




    private List<aadl2_BusAccess> aadl2_busaccesss;


    public aadl2_MemoryType(
    ) {
        super(
        );
        this.aadl2_dataports = new ArrayList<>();
        this.aadl2_eventdataports = new ArrayList<>();
        this.aadl2_busaccesss = new ArrayList<>();
    }

    public aadl2_MemoryType(
        ArrayList<aadl2_DataPort> aadl2_dataports,        ArrayList<aadl2_EventDataPort> aadl2_eventdataports,        ArrayList<aadl2_BusAccess> aadl2_busaccesss    ) {
        this.aadl2_dataports = aadl2_dataports;
        this.aadl2_eventdataports = aadl2_eventdataports;
        this.aadl2_busaccesss = aadl2_busaccesss;
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
    public List<aadl2_BusAccess> getAadl2_busaccesss() {
        return aadl2_busaccesss;
    }

    public void addAadl2_busaccess(Aadl2_busaccess aadl2_busaccess) {
        this.aadl2_busaccesss.add(aadl2_busaccess);
    }

}