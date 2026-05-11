





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Resource extends ItemDefinition {






    private bpmnprof_ResourceRole bpmnprof_resourcerole;




    private List<bpmnprof_ResourceParameter> bpmnprof_resourceparameters;


    public bpmnprof_Resource(
    ) {
        super(
        );
        this.bpmnprof_resourceparameters = new ArrayList<>();
    }

    public bpmnprof_Resource(
        ArrayList<bpmnprof_ResourceParameter> bpmnprof_resourceparameters    ) {
        this.bpmnprof_resourceparameters = bpmnprof_resourceparameters;
    }


    public bpmnprof_ResourceRole getBpmnprof_resourcerole() {
        return bpmnprof_resourcerole;
    }

    public void setBpmnprof_resourcerole(bpmnprof_ResourceRole bpmnprof_resourcerole) {
        this.bpmnprof_resourcerole = bpmnprof_resourcerole;
    }
    public List<bpmnprof_ResourceParameter> getBpmnprof_resourceparameters() {
        return bpmnprof_resourceparameters;
    }

    public void addBpmnprof_resourceparameter(Bpmnprof_resourceparameter bpmnprof_resourceparameter) {
        this.bpmnprof_resourceparameters.add(bpmnprof_resourceparameter);
    }

}