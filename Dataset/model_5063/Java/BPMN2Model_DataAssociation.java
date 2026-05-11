





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataAssociation extends BaseElement {






    private List<BPMN2Model_Assignment> bpmn2model_assignments;


    public BPMN2Model_DataAssociation(
    ) {
        super(
        );
        this.bpmn2model_assignments = new ArrayList<>();
    }

    public BPMN2Model_DataAssociation(
        ArrayList<BPMN2Model_Assignment> bpmn2model_assignments    ) {
        this.bpmn2model_assignments = bpmn2model_assignments;
    }


    public List<BPMN2Model_Assignment> getBpmn2model_assignments() {
        return bpmn2model_assignments;
    }

    public void addBpmn2model_assignment(Bpmn2model_assignment bpmn2model_assignment) {
        this.bpmn2model_assignments.add(bpmn2model_assignment);
    }

}