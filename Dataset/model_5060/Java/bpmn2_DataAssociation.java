





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataAssociation extends BaseElement {






    private List<bpmn2_Assignment> bpmn2_assignments;


    public bpmn2_DataAssociation(
    ) {
        super(
        );
        this.bpmn2_assignments = new ArrayList<>();
    }

    public bpmn2_DataAssociation(
        ArrayList<bpmn2_Assignment> bpmn2_assignments    ) {
        this.bpmn2_assignments = bpmn2_assignments;
    }


    public List<bpmn2_Assignment> getBpmn2_assignments() {
        return bpmn2_assignments;
    }

    public void addBpmn2_assignment(Bpmn2_assignment bpmn2_assignment) {
        this.bpmn2_assignments.add(bpmn2_assignment);
    }

}