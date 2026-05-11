





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ParticipantMultiplicity extends BaseElement {

    private int maximum;
    private int minimum;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Participant bpmn2_participant;


    public bpmn2_ParticipantMultiplicity(
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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Participant getBpmn2_participant() {
        return bpmn2_participant;
    }

    public void setBpmn2_participant(bpmn2_Participant bpmn2_participant) {
        this.bpmn2_participant = bpmn2_participant;
    }

}