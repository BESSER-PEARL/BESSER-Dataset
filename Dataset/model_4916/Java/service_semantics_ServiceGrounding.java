





import java.util.List;
import java.util.ArrayList;

public class service_semantics_ServiceGrounding  {

    private String bindParams;
    private String name;





    private InterfaceDescription interfacedescription;




    private semantics_service_Service semantics_service_service;




    private ProcessModel processmodel;


    public service_semantics_ServiceGrounding(
        String bindParams,        String name    ) {
        this.bindParams = bindParams;
        this.name = name;
    }


    public String getBindparams() {
        return bindParams;
    }

    public void setBindparams(String bindParams) {
        this.bindParams = bindParams;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public InterfaceDescription getInterfacedescription() {
        return interfacedescription;
    }

    public void setInterfacedescription(InterfaceDescription interfacedescription) {
        this.interfacedescription = interfacedescription;
    }
    public semantics_service_Service getSemantics_service_service() {
        return semantics_service_service;
    }

    public void setSemantics_service_service(semantics_service_Service semantics_service_service) {
        this.semantics_service_service = semantics_service_service;
    }
    public ProcessModel getProcessmodel() {
        return processmodel;
    }

    public void setProcessmodel(ProcessModel processmodel) {
        this.processmodel = processmodel;
    }

}