





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Operation extends BaseElement {

    private String name;





    private bpmn2_EObject bpmn2_eobject;


    public bpmn2_Operation(
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

    public bpmn2_EObject getBpmn2_eobject() {
        return bpmn2_eobject;
    }

    public void setBpmn2_eobject(bpmn2_EObject bpmn2_eobject) {
        this.bpmn2_eobject = bpmn2_eobject;
    }

}