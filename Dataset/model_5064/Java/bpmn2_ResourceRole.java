





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ResourceRole extends BaseElement {






    private bpmn2_Activity bpmn2_activity;




    private bpmn2_GlobalTask bpmn2_globaltask;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_ResourceRole(
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
    public bpmn2_GlobalTask getBpmn2_globaltask() {
        return bpmn2_globaltask;
    }

    public void setBpmn2_globaltask(bpmn2_GlobalTask bpmn2_globaltask) {
        this.bpmn2_globaltask = bpmn2_globaltask;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}