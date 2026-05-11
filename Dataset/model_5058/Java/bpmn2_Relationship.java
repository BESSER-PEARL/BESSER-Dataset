





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Relationship extends BaseElement {

    private String type;
    private String direction;





    private List<bpmn2_EObject> bpmn2_eobjects;




    private List<bpmn2_EObject> bpmn2_eobjects;


    public bpmn2_Relationship(
        String type,        String direction    ) {
        super(
        );
        this.type = type;
        this.direction = direction;
        this.bpmn2_eobjects = new ArrayList<>();
        this.bpmn2_eobjects = new ArrayList<>();
    }

    public bpmn2_Relationship(
        String type,        String direction        ArrayList<bpmn2_EObject> bpmn2_eobjects,        ArrayList<bpmn2_EObject> bpmn2_eobjects    ) {
        this.type = type;
        this.direction = direction;
        this.bpmn2_eobjects = bpmn2_eobjects;
        this.bpmn2_eobjects = bpmn2_eobjects;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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

}