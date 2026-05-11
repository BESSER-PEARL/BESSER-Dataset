





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataOutputAssociation extends DataAssociation {






    private BPMN2Model_CatchEvent bpmn2model_catchevent;




    private BPMN2Model_Activity bpmn2model_activity;


    public BPMN2Model_DataOutputAssociation(
    ) {
        super(
        );
    }



    public BPMN2Model_CatchEvent getBpmn2model_catchevent() {
        return bpmn2model_catchevent;
    }

    public void setBpmn2model_catchevent(BPMN2Model_CatchEvent bpmn2model_catchevent) {
        this.bpmn2model_catchevent = bpmn2model_catchevent;
    }
    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }

}