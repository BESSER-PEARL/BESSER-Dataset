





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataOutput extends ItemAwareElement {

    private boolean isCollection;





    private bpmn2_CatchEvent bpmn2_catchevent;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_DataOutput(
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

    public bpmn2_CatchEvent getBpmn2_catchevent() {
        return bpmn2_catchevent;
    }

    public void setBpmn2_catchevent(bpmn2_CatchEvent bpmn2_catchevent) {
        this.bpmn2_catchevent = bpmn2_catchevent;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}