





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ResourceRole extends BaseElement {






    private List<bpmnprof_ResourceParameterBinding> bpmnprof_resourceparameterbindings;




    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;


    public bpmnprof_ResourceRole(
    ) {
        super(
        );
        this.bpmnprof_resourceparameterbindings = new ArrayList<>();
    }

    public bpmnprof_ResourceRole(
        ArrayList<bpmnprof_ResourceParameterBinding> bpmnprof_resourceparameterbindings    ) {
        this.bpmnprof_resourceparameterbindings = bpmnprof_resourceparameterbindings;
    }


    public List<bpmnprof_ResourceParameterBinding> getBpmnprof_resourceparameterbindings() {
        return bpmnprof_resourceparameterbindings;
    }

    public void addBpmnprof_resourceparameterbinding(Bpmnprof_resourceparameterbinding bpmnprof_resourceparameterbinding) {
        this.bpmnprof_resourceparameterbindings.add(bpmnprof_resourceparameterbinding);
    }
    public bpmnprof_BPMNActivity getBpmnprof_bpmnactivity() {
        return bpmnprof_bpmnactivity;
    }

    public void setBpmnprof_bpmnactivity(bpmnprof_BPMNActivity bpmnprof_bpmnactivity) {
        this.bpmnprof_bpmnactivity = bpmnprof_bpmnactivity;
    }

}