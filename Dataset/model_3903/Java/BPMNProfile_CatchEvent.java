





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CatchEvent extends BPMNEvent {

    private String parallelMultiple;





    private List<BPMNProfile_DataOutputAssociation> bpmnprofile_dataoutputassociations;


    public BPMNProfile_CatchEvent(
        String parallelMultiple    ) {
        super(
        );
        this.parallelMultiple = parallelMultiple;
        this.bpmnprofile_dataoutputassociations = new ArrayList<>();
    }

    public BPMNProfile_CatchEvent(
        String parallelMultiple        ArrayList<BPMNProfile_DataOutputAssociation> bpmnprofile_dataoutputassociations    ) {
        this.parallelMultiple = parallelMultiple;
        this.bpmnprofile_dataoutputassociations = bpmnprofile_dataoutputassociations;
    }

    public String getParallelmultiple() {
        return parallelMultiple;
    }

    public void setParallelmultiple(String parallelMultiple) {
        this.parallelMultiple = parallelMultiple;
    }

    public List<BPMNProfile_DataOutputAssociation> getBpmnprofile_dataoutputassociations() {
        return bpmnprofile_dataoutputassociations;
    }

    public void addBpmnprofile_dataoutputassociation(Bpmnprofile_dataoutputassociation bpmnprofile_dataoutputassociation) {
        this.bpmnprofile_dataoutputassociations.add(bpmnprofile_dataoutputassociation);
    }

}