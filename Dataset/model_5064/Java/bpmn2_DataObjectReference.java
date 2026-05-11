





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataObjectReference extends FlowElement, ItemAwareElement {






    private bpmn2_DataObject bpmn2_dataobject;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_DataObjectReference(
    ) {
        super(
        );
    }



    public bpmn2_DataObject getBpmn2_dataobject() {
        return bpmn2_dataobject;
    }

    public void setBpmn2_dataobject(bpmn2_DataObject bpmn2_dataobject) {
        this.bpmn2_dataobject = bpmn2_dataobject;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}