





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessorType extends ComponentType, ProcessorClassifier {






    private List<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss;




    private List<aadl2_EventPort> aadl2_eventports;




    private List<aadl2_EventDataPort> aadl2_eventdataports;




    private List<aadl2_SubprogramAccess> aadl2_subprogramaccesss;




    private List<aadl2_BusAccess> aadl2_busaccesss;




    private List<aadl2_DataPort> aadl2_dataports;


    public aadl2_ProcessorType(
    ) {
        super(
        );
        this.aadl2_subprogramgroupaccesss = new ArrayList<>();
        this.aadl2_eventports = new ArrayList<>();
        this.aadl2_eventdataports = new ArrayList<>();
        this.aadl2_subprogramaccesss = new ArrayList<>();
        this.aadl2_busaccesss = new ArrayList<>();
        this.aadl2_dataports = new ArrayList<>();
    }

    public aadl2_ProcessorType(
        ArrayList<aadl2_SubprogramGroupAccess> aadl2_subprogramgroupaccesss,        ArrayList<aadl2_EventPort> aadl2_eventports,        ArrayList<aadl2_EventDataPort> aadl2_eventdataports,        ArrayList<aadl2_SubprogramAccess> aadl2_subprogramaccesss,        ArrayList<aadl2_BusAccess> aadl2_busaccesss,        ArrayList<aadl2_DataPort> aadl2_dataports    ) {
        this.aadl2_subprogramgroupaccesss = aadl2_subprogramgroupaccesss;
        this.aadl2_eventports = aadl2_eventports;
        this.aadl2_eventdataports = aadl2_eventdataports;
        this.aadl2_subprogramaccesss = aadl2_subprogramaccesss;
        this.aadl2_busaccesss = aadl2_busaccesss;
        this.aadl2_dataports = aadl2_dataports;
    }


    public List<aadl2_SubprogramGroupAccess> getAadl2_subprogramgroupaccesss() {
        return aadl2_subprogramgroupaccesss;
    }

    public void addAadl2_subprogramgroupaccess(Aadl2_subprogramgroupaccess aadl2_subprogramgroupaccess) {
        this.aadl2_subprogramgroupaccesss.add(aadl2_subprogramgroupaccess);
    }
    public List<aadl2_EventPort> getAadl2_eventports() {
        return aadl2_eventports;
    }

    public void addAadl2_eventport(Aadl2_eventport aadl2_eventport) {
        this.aadl2_eventports.add(aadl2_eventport);
    }
    public List<aadl2_EventDataPort> getAadl2_eventdataports() {
        return aadl2_eventdataports;
    }

    public void addAadl2_eventdataport(Aadl2_eventdataport aadl2_eventdataport) {
        this.aadl2_eventdataports.add(aadl2_eventdataport);
    }
    public List<aadl2_SubprogramAccess> getAadl2_subprogramaccesss() {
        return aadl2_subprogramaccesss;
    }

    public void addAadl2_subprogramaccess(Aadl2_subprogramaccess aadl2_subprogramaccess) {
        this.aadl2_subprogramaccesss.add(aadl2_subprogramaccess);
    }
    public List<aadl2_BusAccess> getAadl2_busaccesss() {
        return aadl2_busaccesss;
    }

    public void addAadl2_busaccess(Aadl2_busaccess aadl2_busaccess) {
        this.aadl2_busaccesss.add(aadl2_busaccess);
    }
    public List<aadl2_DataPort> getAadl2_dataports() {
        return aadl2_dataports;
    }

    public void addAadl2_dataport(Aadl2_dataport aadl2_dataport) {
        this.aadl2_dataports.add(aadl2_dataport);
    }

}