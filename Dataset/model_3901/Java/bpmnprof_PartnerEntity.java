





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_PartnerEntity extends RootElement {






    private bpmnprof_Participant bpmnprof_participant;




    private List<bpmnprof_Participant> bpmnprof_participants;


    public bpmnprof_PartnerEntity(
    ) {
        super(
        );
        this.bpmnprof_participants = new ArrayList<>();
    }

    public bpmnprof_PartnerEntity(
        ArrayList<bpmnprof_Participant> bpmnprof_participants    ) {
        this.bpmnprof_participants = bpmnprof_participants;
    }


    public bpmnprof_Participant getBpmnprof_participant() {
        return bpmnprof_participant;
    }

    public void setBpmnprof_participant(bpmnprof_Participant bpmnprof_participant) {
        this.bpmnprof_participant = bpmnprof_participant;
    }
    public List<bpmnprof_Participant> getBpmnprof_participants() {
        return bpmnprof_participants;
    }

    public void addBpmnprof_participant(Bpmnprof_participant bpmnprof_participant) {
        this.bpmnprof_participants.add(bpmnprof_participant);
    }

}