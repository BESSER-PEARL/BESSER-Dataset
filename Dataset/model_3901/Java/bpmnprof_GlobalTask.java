





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_GlobalTask extends CallableElement {






    private List<bpmnprof_ResourceRole> bpmnprof_resourceroles;


    public bpmnprof_GlobalTask(
    ) {
        super(
        );
        this.bpmnprof_resourceroles = new ArrayList<>();
    }

    public bpmnprof_GlobalTask(
        ArrayList<bpmnprof_ResourceRole> bpmnprof_resourceroles    ) {
        this.bpmnprof_resourceroles = bpmnprof_resourceroles;
    }


    public List<bpmnprof_ResourceRole> getBpmnprof_resourceroles() {
        return bpmnprof_resourceroles;
    }

    public void addBpmnprof_resourcerole(Bpmnprof_resourcerole bpmnprof_resourcerole) {
        this.bpmnprof_resourceroles.add(bpmnprof_resourcerole);
    }

}