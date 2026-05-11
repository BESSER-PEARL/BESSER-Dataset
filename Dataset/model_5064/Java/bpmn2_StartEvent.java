





import java.util.List;
import java.util.ArrayList;

public class bpmn2_StartEvent extends CatchEvent {

    private boolean isInterrupting;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_StartEvent(
        boolean isInterrupting    ) {
        super(
        );
        this.isInterrupting = isInterrupting;
    }


    public boolean getIsinterrupting() {
        return isInterrupting;
    }

    public void setIsinterrupting(boolean isInterrupting) {
        this.isInterrupting = isInterrupting;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}