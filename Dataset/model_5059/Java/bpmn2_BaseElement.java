





import java.util.List;
import java.util.ArrayList;

public class bpmn2_BaseElement  {

    private String id;
    private String description;





    private bpmn2_Lane bpmn2_lane;




    private bpmn2_Lane bpmn2_lane;




    private List<bpmn2_Documentation> bpmn2_documentations;


    public bpmn2_BaseElement(
        String id,        String description    ) {
        this.id = id;
        this.description = description;
        this.bpmn2_documentations = new ArrayList<>();
    }

    public bpmn2_BaseElement(
        String id,        String description        ArrayList<bpmn2_Documentation> bpmn2_documentations    ) {
        this.id = id;
        this.description = description;
        this.bpmn2_documentations = bpmn2_documentations;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public List<bpmn2_Documentation> getBpmn2_documentations() {
        return bpmn2_documentations;
    }

    public void addBpmn2_documentation(Bpmn2_documentation bpmn2_documentation) {
        this.bpmn2_documentations.add(bpmn2_documentation);
    }

}