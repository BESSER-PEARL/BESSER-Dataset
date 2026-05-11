





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Relationship extends BaseElement {

    private String direction;
    private String type;





    private List<bpmn2_EObject> bpmn2_eobjects;




    private List<bpmn2_EObject> bpmn2_eobjects;




    private bpmn2_Definitions bpmn2_definitions;


    public bpmn2_Relationship(
        String direction,        String type    ) {
        super(
        );
        this.direction = direction;
        this.type = type;
        this.bpmn2_eobjects = new ArrayList<>();
        this.bpmn2_eobjects = new ArrayList<>();
    }

    public bpmn2_Relationship(
        String direction,        String type        ArrayList<bpmn2_EObject> bpmn2_eobjects,        ArrayList<bpmn2_EObject> bpmn2_eobjects    ) {
        this.direction = direction;
        this.type = type;
        this.bpmn2_eobjects = bpmn2_eobjects;
        this.bpmn2_eobjects = bpmn2_eobjects;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<bpmn2_EObject> getBpmn2_eobjects() {
        return bpmn2_eobjects;
    }

    public void addBpmn2_eobject(Bpmn2_eobject bpmn2_eobject) {
        this.bpmn2_eobjects.add(bpmn2_eobject);
    }
    public List<bpmn2_EObject> getBpmn2_eobjects() {
        return bpmn2_eobjects;
    }

    public void addBpmn2_eobject(Bpmn2_eobject bpmn2_eobject) {
        this.bpmn2_eobjects.add(bpmn2_eobject);
    }
    public bpmn2_Definitions getBpmn2_definitions() {
        return bpmn2_definitions;
    }

    public void setBpmn2_definitions(bpmn2_Definitions bpmn2_definitions) {
        this.bpmn2_definitions = bpmn2_definitions;
    }

}