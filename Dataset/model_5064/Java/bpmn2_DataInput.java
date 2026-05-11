





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataInput extends ItemAwareElement {

    private boolean isCollection;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_DataInput(
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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}