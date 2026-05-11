





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataObject extends FlowElement, ItemAwareElement {

    private String isCollection;



    public bpmnprof_DataObject(
        String isCollection    ) {
        super(
        );
        this.isCollection = isCollection;
    }


    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }


}