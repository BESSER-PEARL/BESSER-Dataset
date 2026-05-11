





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ParticipantMultiplicity extends BaseElement {

    private String minimum;
    private String maximum;





    private BPMNProfile_Participant bpmnprofile_participant;


    public BPMNProfile_ParticipantMultiplicity(
        String minimum,        String maximum    ) {
        super(
        );
        this.minimum = minimum;
        this.maximum = maximum;
    }


    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }

    public BPMNProfile_Participant getBpmnprofile_participant() {
        return bpmnprofile_participant;
    }

    public void setBpmnprofile_participant(BPMNProfile_Participant bpmnprofile_participant) {
        this.bpmnprofile_participant = bpmnprofile_participant;
    }

}