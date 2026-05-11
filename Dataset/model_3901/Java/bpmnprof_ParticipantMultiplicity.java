





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ParticipantMultiplicity extends BaseElement {

    private String maximum;
    private String minimum;





    private bpmnprof_Participant bpmnprof_participant;


    public bpmnprof_ParticipantMultiplicity(
        String maximum,        String minimum    ) {
        super(
        );
        this.maximum = maximum;
        this.minimum = minimum;
    }


    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }

    public bpmnprof_Participant getBpmnprof_participant() {
        return bpmnprof_participant;
    }

    public void setBpmnprof_participant(bpmnprof_Participant bpmnprof_participant) {
        this.bpmnprof_participant = bpmnprof_participant;
    }

}