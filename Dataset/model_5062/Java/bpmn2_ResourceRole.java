





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ResourceRole extends BaseElement {

    private String name;





    private bpmn2_Resource bpmn2_resource;


    public bpmn2_ResourceRole(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_Resource getBpmn2_resource() {
        return bpmn2_resource;
    }

    public void setBpmn2_resource(bpmn2_Resource bpmn2_resource) {
        this.bpmn2_resource = bpmn2_resource;
    }

}