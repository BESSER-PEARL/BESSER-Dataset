





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CatchEvent extends Event {

    private boolean parallelMultiple;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_CatchEvent(
        boolean parallelMultiple    ) {
        super(
        );
        this.parallelMultiple = parallelMultiple;
    }


    public boolean getParallelmultiple() {
        return parallelMultiple;
    }

    public void setParallelmultiple(boolean parallelMultiple) {
        this.parallelMultiple = parallelMultiple;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}