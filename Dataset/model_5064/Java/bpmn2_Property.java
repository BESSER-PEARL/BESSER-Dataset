





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Property extends ItemAwareElement {






    private bpmn2_Activity bpmn2_activity;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Event bpmn2_event;


    public bpmn2_Property(
    ) {
        super(
        );
    }



    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Event getBpmn2_event() {
        return bpmn2_event;
    }

    public void setBpmn2_event(bpmn2_Event bpmn2_event) {
        this.bpmn2_event = bpmn2_event;
    }

}