





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataObject extends FlowElement, ItemAwareElement {

    private boolean isCollection;



    public BPMN2Model_DataObject(
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