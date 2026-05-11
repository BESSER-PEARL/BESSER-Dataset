





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CallableElement extends RootElement {

    private String name;





    private bpmn2_CallActivity bpmn2_callactivity;


    public bpmn2_CallableElement(
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

    public bpmn2_CallActivity getBpmn2_callactivity() {
        return bpmn2_callactivity;
    }

    public void setBpmn2_callactivity(bpmn2_CallActivity bpmn2_callactivity) {
        this.bpmn2_callactivity = bpmn2_callactivity;
    }

}