





import java.util.List;
import java.util.ArrayList;

public class bpmn2_MessageEventDefinition extends EventDefinition {






    private bpmn2_Message bpmn2_message;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_MessageEventDefinition(
    ) {
        super(
        );
    }



    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}