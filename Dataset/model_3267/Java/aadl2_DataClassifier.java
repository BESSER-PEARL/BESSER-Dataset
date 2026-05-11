





import java.util.List;
import java.util.ArrayList;

public class aadl2_DataClassifier extends DataSubcomponentType, ComponentClassifier, Data {






    private aadl2_EventDataSource aadl2_eventdatasource;




    private aadl2_PortProxy aadl2_portproxy;


    public aadl2_DataClassifier(
    ) {
        super(
        );
    }



    public aadl2_EventDataSource getAadl2_eventdatasource() {
        return aadl2_eventdatasource;
    }

    public void setAadl2_eventdatasource(aadl2_EventDataSource aadl2_eventdatasource) {
        this.aadl2_eventdatasource = aadl2_eventdatasource;
    }
    public aadl2_PortProxy getAadl2_portproxy() {
        return aadl2_portproxy;
    }

    public void setAadl2_portproxy(aadl2_PortProxy aadl2_portproxy) {
        this.aadl2_portproxy = aadl2_portproxy;
    }

}