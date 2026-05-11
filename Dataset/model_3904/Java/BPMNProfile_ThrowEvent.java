





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ThrowEvent extends BPMNEvent {






    private List<BPMNProfile_DataInputAssociation> bpmnprofile_datainputassociations;


    public BPMNProfile_ThrowEvent(
    ) {
        super(
        );
        this.bpmnprofile_datainputassociations = new ArrayList<>();
    }

    public BPMNProfile_ThrowEvent(
        ArrayList<BPMNProfile_DataInputAssociation> bpmnprofile_datainputassociations    ) {
        this.bpmnprofile_datainputassociations = bpmnprofile_datainputassociations;
    }


    public List<BPMNProfile_DataInputAssociation> getBpmnprofile_datainputassociations() {
        return bpmnprofile_datainputassociations;
    }

    public void addBpmnprofile_datainputassociation(Bpmnprofile_datainputassociation bpmnprofile_datainputassociation) {
        this.bpmnprofile_datainputassociations.add(bpmnprofile_datainputassociation);
    }

}