





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataObject extends FlowElement, ItemAwareElement {

    private boolean isCollection;



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


}