





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataOutputAssociation extends DataAssociation {






    private bpmn2_Activity bpmn2_activity;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_CatchEvent bpmn2_catchevent;


    public bpmn2_DataOutputAssociation(
    ) {
        super(
        );
    }



    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_CatchEvent getBpmn2_catchevent() {
        return bpmn2_catchevent;
    }

    public void setBpmn2_catchevent(bpmn2_CatchEvent bpmn2_catchevent) {
        this.bpmn2_catchevent = bpmn2_catchevent;
    }

}