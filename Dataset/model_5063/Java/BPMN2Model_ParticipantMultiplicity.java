





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ParticipantMultiplicity extends BPMNBase {

    private int maximum;
    private int minimum;





    private BPMN2Model_Participant bpmn2model_participant;


    public BPMN2Model_ParticipantMultiplicity(
        int maximum,        int minimum    ) {
        super(
        );
        this.maximum = maximum;
        this.minimum = minimum;
    }


    public int getMaximum() {
        return maximum;
    }

    public void setMaximum(int maximum) {
        this.maximum = maximum;
    }
    public int getMinimum() {
        return minimum;
    }

    public void setMinimum(int minimum) {
        this.minimum = minimum;
    }

    public BPMN2Model_Participant getBpmn2model_participant() {
        return bpmn2model_participant;
    }

    public void setBpmn2model_participant(BPMN2Model_Participant bpmn2model_participant) {
        this.bpmn2model_participant = bpmn2model_participant;
    }

}