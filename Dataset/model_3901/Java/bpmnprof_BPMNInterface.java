





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNInterface extends RootElement {






    private List<bpmnprof_BPMNOperation> bpmnprof_bpmnoperations;




    private bpmnprof_CallableElement bpmnprof_callableelement;




    private List<bpmnprof_CallableElement> bpmnprof_callableelements;




    private bpmnprof_Participant bpmnprof_participant;




    private bpmnprof_Element bpmnprof_element;


    public bpmnprof_BPMNInterface(
    ) {
        super(
        );
        this.bpmnprof_bpmnoperations = new ArrayList<>();
        this.bpmnprof_callableelements = new ArrayList<>();
    }

    public bpmnprof_BPMNInterface(
        ArrayList<bpmnprof_BPMNOperation> bpmnprof_bpmnoperations,        ArrayList<bpmnprof_CallableElement> bpmnprof_callableelements    ) {
        this.bpmnprof_bpmnoperations = bpmnprof_bpmnoperations;
        this.bpmnprof_callableelements = bpmnprof_callableelements;
    }


    public List<bpmnprof_BPMNOperation> getBpmnprof_bpmnoperations() {
        return bpmnprof_bpmnoperations;
    }

    public void addBpmnprof_bpmnoperation(Bpmnprof_bpmnoperation bpmnprof_bpmnoperation) {
        this.bpmnprof_bpmnoperations.add(bpmnprof_bpmnoperation);
    }
    public bpmnprof_CallableElement getBpmnprof_callableelement() {
        return bpmnprof_callableelement;
    }

    public void setBpmnprof_callableelement(bpmnprof_CallableElement bpmnprof_callableelement) {
        this.bpmnprof_callableelement = bpmnprof_callableelement;
    }
    public List<bpmnprof_CallableElement> getBpmnprof_callableelements() {
        return bpmnprof_callableelements;
    }

    public void addBpmnprof_callableelement(Bpmnprof_callableelement bpmnprof_callableelement) {
        this.bpmnprof_callableelements.add(bpmnprof_callableelement);
    }
    public bpmnprof_Participant getBpmnprof_participant() {
        return bpmnprof_participant;
    }

    public void setBpmnprof_participant(bpmnprof_Participant bpmnprof_participant) {
        this.bpmnprof_participant = bpmnprof_participant;
    }
    public bpmnprof_Element getBpmnprof_element() {
        return bpmnprof_element;
    }

    public void setBpmnprof_element(bpmnprof_Element bpmnprof_element) {
        this.bpmnprof_element = bpmnprof_element;
    }

}