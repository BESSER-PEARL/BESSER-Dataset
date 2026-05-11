





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataAssociation extends BaseElement {






    private bpmn2_ItemAwareElement bpmn2_itemawareelement;




    private List<bpmn2_ItemAwareElement> bpmn2_itemawareelements;




    private List<bpmn2_Assignment> bpmn2_assignments;


    public bpmn2_DataAssociation(
    ) {
        super(
        );
        this.bpmn2_itemawareelements = new ArrayList<>();
        this.bpmn2_assignments = new ArrayList<>();
    }

    public bpmn2_DataAssociation(
        ArrayList<bpmn2_ItemAwareElement> bpmn2_itemawareelements,        ArrayList<bpmn2_Assignment> bpmn2_assignments    ) {
        this.bpmn2_itemawareelements = bpmn2_itemawareelements;
        this.bpmn2_assignments = bpmn2_assignments;
    }


    public bpmn2_ItemAwareElement getBpmn2_itemawareelement() {
        return bpmn2_itemawareelement;
    }

    public void setBpmn2_itemawareelement(bpmn2_ItemAwareElement bpmn2_itemawareelement) {
        this.bpmn2_itemawareelement = bpmn2_itemawareelement;
    }
    public List<bpmn2_ItemAwareElement> getBpmn2_itemawareelements() {
        return bpmn2_itemawareelements;
    }

    public void addBpmn2_itemawareelement(Bpmn2_itemawareelement bpmn2_itemawareelement) {
        this.bpmn2_itemawareelements.add(bpmn2_itemawareelement);
    }
    public List<bpmn2_Assignment> getBpmn2_assignments() {
        return bpmn2_assignments;
    }

    public void addBpmn2_assignment(Bpmn2_assignment bpmn2_assignment) {
        this.bpmn2_assignments.add(bpmn2_assignment);
    }

}