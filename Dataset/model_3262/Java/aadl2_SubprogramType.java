





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramType extends CallContext, SubprogramClassifier, ComponentType {






    private List<aadl2_DataAccess> aadl2_dataaccesss;




    private List<aadl2_EventDataPort> aadl2_eventdataports;




    private List<aadl2_Parameter> aadl2_parameters;


    public aadl2_SubprogramType(
    ) {
        super(
        );
        this.aadl2_dataaccesss = new ArrayList<>();
        this.aadl2_eventdataports = new ArrayList<>();
        this.aadl2_parameters = new ArrayList<>();
    }

    public aadl2_SubprogramType(
        ArrayList<aadl2_DataAccess> aadl2_dataaccesss,        ArrayList<aadl2_EventDataPort> aadl2_eventdataports,        ArrayList<aadl2_Parameter> aadl2_parameters    ) {
        this.aadl2_dataaccesss = aadl2_dataaccesss;
        this.aadl2_eventdataports = aadl2_eventdataports;
        this.aadl2_parameters = aadl2_parameters;
    }


    public List<aadl2_DataAccess> getAadl2_dataaccesss() {
        return aadl2_dataaccesss;
    }

    public void addAadl2_dataaccess(Aadl2_dataaccess aadl2_dataaccess) {
        this.aadl2_dataaccesss.add(aadl2_dataaccess);
    }
    public List<aadl2_EventDataPort> getAadl2_eventdataports() {
        return aadl2_eventdataports;
    }

    public void addAadl2_eventdataport(Aadl2_eventdataport aadl2_eventdataport) {
        this.aadl2_eventdataports.add(aadl2_eventdataport);
    }
    public List<aadl2_Parameter> getAadl2_parameters() {
        return aadl2_parameters;
    }

    public void addAadl2_parameter(Aadl2_parameter aadl2_parameter) {
        this.aadl2_parameters.add(aadl2_parameter);
    }

}