





import java.util.List;
import java.util.ArrayList;

public class service_semantics_ServiceProfile  {

    private String serviceClassification;
    private String name;





    private ProcessModel processmodel;


    public service_semantics_ServiceProfile(
        String serviceClassification,        String name    ) {
        this.serviceClassification = serviceClassification;
        this.name = name;
    }


    public String getServiceclassification() {
        return serviceClassification;
    }

    public void setServiceclassification(String serviceClassification) {
        this.serviceClassification = serviceClassification;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ProcessModel getProcessmodel() {
        return processmodel;
    }

    public void setProcessmodel(ProcessModel processmodel) {
        this.processmodel = processmodel;
    }

}