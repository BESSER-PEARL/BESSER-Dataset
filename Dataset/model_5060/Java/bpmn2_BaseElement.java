





import java.util.List;
import java.util.ArrayList;

public class bpmn2_BaseElement  {

    private String description;
    private String id;





    private bpmn2_Lane bpmn2_lane;




    private bpmn2_Lane bpmn2_lane;




    private bpmn2_Association bpmn2_association;




    private List<bpmn2_Documentation> bpmn2_documentations;




    private bpmn2_Association bpmn2_association;


    public bpmn2_BaseElement(
        String description,        String id    ) {
        this.description = description;
        this.id = id;
        this.bpmn2_documentations = new ArrayList<>();
    }

    public bpmn2_BaseElement(
        String description,        String id        ArrayList<bpmn2_Documentation> bpmn2_documentations    ) {
        this.description = description;
        this.id = id;
        this.bpmn2_documentations = bpmn2_documentations;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_Lane getBpmn2_lane() {
        return bpmn2_lane;
    }

    public void setBpmn2_lane(bpmn2_Lane bpmn2_lane) {
        this.bpmn2_lane = bpmn2_lane;
    }
    public bpmn2_Lane getBpmn2_lane() {
        return bpmn2_lane;
    }

    public void setBpmn2_lane(bpmn2_Lane bpmn2_lane) {
        this.bpmn2_lane = bpmn2_lane;
    }
    public bpmn2_Association getBpmn2_association() {
        return bpmn2_association;
    }

    public void setBpmn2_association(bpmn2_Association bpmn2_association) {
        this.bpmn2_association = bpmn2_association;
    }
    public List<bpmn2_Documentation> getBpmn2_documentations() {
        return bpmn2_documentations;
    }

    public void addBpmn2_documentation(Bpmn2_documentation bpmn2_documentation) {
        this.bpmn2_documentations.add(bpmn2_documentation);
    }
    public bpmn2_Association getBpmn2_association() {
        return bpmn2_association;
    }

    public void setBpmn2_association(bpmn2_Association bpmn2_association) {
        this.bpmn2_association = bpmn2_association;
    }

}