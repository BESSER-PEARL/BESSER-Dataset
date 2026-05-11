





import java.util.List;
import java.util.ArrayList;

public class service_semantics_IOEP  {






    private List<ServiceInput> serviceinputs;




    private List<ServiceCondition> serviceconditions;




    private List<ServiceResult> serviceresults;




    private List<ServiceOutput> serviceoutputs;


    public service_semantics_IOEP(
    ) {
        this.serviceinputs = new ArrayList<>();
        this.serviceconditions = new ArrayList<>();
        this.serviceresults = new ArrayList<>();
        this.serviceoutputs = new ArrayList<>();
    }

    public service_semantics_IOEP(
        ArrayList<ServiceInput> serviceinputs,        ArrayList<ServiceCondition> serviceconditions,        ArrayList<ServiceResult> serviceresults,        ArrayList<ServiceOutput> serviceoutputs    ) {
        this.serviceinputs = serviceinputs;
        this.serviceconditions = serviceconditions;
        this.serviceresults = serviceresults;
        this.serviceoutputs = serviceoutputs;
    }


    public List<ServiceInput> getServiceinputs() {
        return serviceinputs;
    }

    public void addServiceinput(Serviceinput serviceinput) {
        this.serviceinputs.add(serviceinput);
    }
    public List<ServiceCondition> getServiceconditions() {
        return serviceconditions;
    }

    public void addServicecondition(Servicecondition servicecondition) {
        this.serviceconditions.add(servicecondition);
    }
    public List<ServiceResult> getServiceresults() {
        return serviceresults;
    }

    public void addServiceresult(Serviceresult serviceresult) {
        this.serviceresults.add(serviceresult);
    }
    public List<ServiceOutput> getServiceoutputs() {
        return serviceoutputs;
    }

    public void addServiceoutput(Serviceoutput serviceoutput) {
        this.serviceoutputs.add(serviceoutput);
    }

}