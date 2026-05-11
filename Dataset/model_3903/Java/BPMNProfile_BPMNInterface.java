





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNInterface extends RootElement {






    private BPMNProfile_Element bpmnprofile_element;




    private List<BPMNProfile_BPMNOperation> bpmnprofile_bpmnoperations;




    private BPMNProfile_Participant bpmnprofile_participant;


    public BPMNProfile_BPMNInterface(
    ) {
        super(
        );
        this.bpmnprofile_bpmnoperations = new ArrayList<>();
    }

    public BPMNProfile_BPMNInterface(
        ArrayList<BPMNProfile_BPMNOperation> bpmnprofile_bpmnoperations    ) {
        this.bpmnprofile_bpmnoperations = bpmnprofile_bpmnoperations;
    }


    public BPMNProfile_Element getBpmnprofile_element() {
        return bpmnprofile_element;
    }

    public void setBpmnprofile_element(BPMNProfile_Element bpmnprofile_element) {
        this.bpmnprofile_element = bpmnprofile_element;
    }
    public List<BPMNProfile_BPMNOperation> getBpmnprofile_bpmnoperations() {
        return bpmnprofile_bpmnoperations;
    }

    public void addBpmnprofile_bpmnoperation(Bpmnprofile_bpmnoperation bpmnprofile_bpmnoperation) {
        this.bpmnprofile_bpmnoperations.add(bpmnprofile_bpmnoperation);
    }
    public BPMNProfile_Participant getBpmnprofile_participant() {
        return bpmnprofile_participant;
    }

    public void setBpmnprofile_participant(BPMNProfile_Participant bpmnprofile_participant) {
        this.bpmnprofile_participant = bpmnprofile_participant;
    }

}