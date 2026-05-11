





import java.util.List;
import java.util.ArrayList;

public class smachDSL_ServiceClient  {

    private String servicesrv;
    private String servicename;
    private String name;





    private smachDSL_StateMachine smachdsl_statemachine;


    public smachDSL_ServiceClient(
        String servicesrv,        String servicename,        String name    ) {
        this.servicesrv = servicesrv;
        this.servicename = servicename;
        this.name = name;
    }


    public String getServicesrv() {
        return servicesrv;
    }

    public void setServicesrv(String servicesrv) {
        this.servicesrv = servicesrv;
    }
    public String getServicename() {
        return servicename;
    }

    public void setServicename(String servicename) {
        this.servicename = servicename;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smachDSL_StateMachine getSmachdsl_statemachine() {
        return smachdsl_statemachine;
    }

    public void setSmachdsl_statemachine(smachDSL_StateMachine smachdsl_statemachine) {
        this.smachdsl_statemachine = smachdsl_statemachine;
    }

}