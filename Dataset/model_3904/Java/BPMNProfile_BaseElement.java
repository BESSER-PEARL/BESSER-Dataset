





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BaseElement  {

    private String id;





    private List<BPMNProfile_Documentation> bpmnprofile_documentations;




    private BPMNProfile_Lane bpmnprofile_lane;


    public BPMNProfile_BaseElement(
        String id    ) {
        this.id = id;
        this.bpmnprofile_documentations = new ArrayList<>();
    }

    public BPMNProfile_BaseElement(
        String id        ArrayList<BPMNProfile_Documentation> bpmnprofile_documentations    ) {
        this.id = id;
        this.bpmnprofile_documentations = bpmnprofile_documentations;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<BPMNProfile_Documentation> getBpmnprofile_documentations() {
        return bpmnprofile_documentations;
    }

    public void addBpmnprofile_documentation(Bpmnprofile_documentation bpmnprofile_documentation) {
        this.bpmnprofile_documentations.add(bpmnprofile_documentation);
    }
    public BPMNProfile_Lane getBpmnprofile_lane() {
        return bpmnprofile_lane;
    }

    public void setBpmnprofile_lane(BPMNProfile_Lane bpmnprofile_lane) {
        this.bpmnprofile_lane = bpmnprofile_lane;
    }

}