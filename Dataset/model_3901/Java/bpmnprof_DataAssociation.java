





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataAssociation extends BaseElement {






    private List<bpmnprof_Assignment> bpmnprof_assignments;


    public bpmnprof_DataAssociation(
    ) {
        super(
        );
        this.bpmnprof_assignments = new ArrayList<>();
    }

    public bpmnprof_DataAssociation(
        ArrayList<bpmnprof_Assignment> bpmnprof_assignments    ) {
        this.bpmnprof_assignments = bpmnprof_assignments;
    }


    public List<bpmnprof_Assignment> getBpmnprof_assignments() {
        return bpmnprof_assignments;
    }

    public void addBpmnprof_assignment(Bpmnprof_assignment bpmnprof_assignment) {
        this.bpmnprof_assignments.add(bpmnprof_assignment);
    }

}