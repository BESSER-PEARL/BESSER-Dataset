





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ParticipantMultiplicity  {

    private int minimum;
    private int maximum;
    private String id;





    private bpmn2_Participant bpmn2_participant;


    public bpmn2_ParticipantMultiplicity(
        int minimum,        int maximum,        String id    ) {
        this.minimum = minimum;
        this.maximum = maximum;
        this.id = id;
    }


    public int getMinimum() {
        return minimum;
    }

    public void setMinimum(int minimum) {
        this.minimum = minimum;
    }
    public int getMaximum() {
        return maximum;
    }

    public void setMaximum(int maximum) {
        this.maximum = maximum;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_Participant getBpmn2_participant() {
        return bpmn2_participant;
    }

    public void setBpmn2_participant(bpmn2_Participant bpmn2_participant) {
        this.bpmn2_participant = bpmn2_participant;
    }

}