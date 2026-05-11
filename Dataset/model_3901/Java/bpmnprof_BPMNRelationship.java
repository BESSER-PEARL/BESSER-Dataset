





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNRelationship extends BaseElement {

    private String direction;
    private String type;





    private List<bpmnprof_Element> bpmnprof_elements;




    private List<bpmnprof_Element> bpmnprof_elements;


    public bpmnprof_BPMNRelationship(
        String direction,        String type    ) {
        super(
        );
        this.direction = direction;
        this.type = type;
        this.bpmnprof_elements = new ArrayList<>();
        this.bpmnprof_elements = new ArrayList<>();
    }

    public bpmnprof_BPMNRelationship(
        String direction,        String type        ArrayList<bpmnprof_Element> bpmnprof_elements,        ArrayList<bpmnprof_Element> bpmnprof_elements    ) {
        this.direction = direction;
        this.type = type;
        this.bpmnprof_elements = bpmnprof_elements;
        this.bpmnprof_elements = bpmnprof_elements;
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

    public List<bpmnprof_Element> getBpmnprof_elements() {
        return bpmnprof_elements;
    }

    public void addBpmnprof_element(Bpmnprof_element bpmnprof_element) {
        this.bpmnprof_elements.add(bpmnprof_element);
    }
    public List<bpmnprof_Element> getBpmnprof_elements() {
        return bpmnprof_elements;
    }

    public void addBpmnprof_element(Bpmnprof_element bpmnprof_element) {
        this.bpmnprof_elements.add(bpmnprof_element);
    }

}