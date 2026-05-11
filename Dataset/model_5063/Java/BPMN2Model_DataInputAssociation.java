





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataInputAssociation extends DataAssociation {






    private BPMN2Model_ThrowEvent bpmn2model_throwevent;




    private BPMN2Model_Activity bpmn2model_activity;


    public BPMN2Model_DataInputAssociation(
    ) {
        super(
        );
    }



    public BPMN2Model_ThrowEvent getBpmn2model_throwevent() {
        return bpmn2model_throwevent;
    }

    public void setBpmn2model_throwevent(BPMN2Model_ThrowEvent bpmn2model_throwevent) {
        this.bpmn2model_throwevent = bpmn2model_throwevent;
    }
    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }

}