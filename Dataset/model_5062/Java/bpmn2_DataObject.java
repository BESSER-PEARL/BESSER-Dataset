





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataObject extends FlowElement, ItemAwareElement {

    private boolean isCollection;





    private bpmn2_DataObjectReference bpmn2_dataobjectreference;


    public bpmn2_DataObject(
        boolean isCollection    ) {
        super(
        );
        this.isCollection = isCollection;
    }


    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }

    public bpmn2_DataObjectReference getBpmn2_dataobjectreference() {
        return bpmn2_dataobjectreference;
    }

    public void setBpmn2_dataobjectreference(bpmn2_DataObjectReference bpmn2_dataobjectreference) {
        this.bpmn2_dataobjectreference = bpmn2_dataobjectreference;
    }

}