





import java.util.List;
import java.util.ArrayList;

public class aadl2_AbstractType extends CallContext, ComponentType, AbstractClassifier {






    private List<aadl2_DataAccess> aadl2_dataaccesss;




    private List<aadl2_DataPort> aadl2_dataports;




    private List<aadl2_EventDataPort> aadl2_eventdataports;


    public aadl2_AbstractType(
    ) {
        super(
        );
        this.aadl2_dataaccesss = new ArrayList<>();
        this.aadl2_dataports = new ArrayList<>();
        this.aadl2_eventdataports = new ArrayList<>();
    }

    public aadl2_AbstractType(
        ArrayList<aadl2_DataAccess> aadl2_dataaccesss,        ArrayList<aadl2_DataPort> aadl2_dataports,        ArrayList<aadl2_EventDataPort> aadl2_eventdataports    ) {
        this.aadl2_dataaccesss = aadl2_dataaccesss;
        this.aadl2_dataports = aadl2_dataports;
        this.aadl2_eventdataports = aadl2_eventdataports;
    }


    public List<aadl2_DataAccess> getAadl2_dataaccesss() {
        return aadl2_dataaccesss;
    }

    public void addAadl2_dataaccess(Aadl2_dataaccess aadl2_dataaccess) {
        this.aadl2_dataaccesss.add(aadl2_dataaccess);
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

}