





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_PartnerRole extends RootElement {






    private List<bpmnprof_Participant> bpmnprof_participants;




    private bpmnprof_Class bpmnprof_class;




    private bpmnprof_Participant bpmnprof_participant;


    public bpmnprof_PartnerRole(
    ) {
        super(
        );
        this.bpmnprof_participants = new ArrayList<>();
    }

    public bpmnprof_PartnerRole(
        ArrayList<bpmnprof_Participant> bpmnprof_participants    ) {
        this.bpmnprof_participants = bpmnprof_participants;
    }


    public List<bpmnprof_Participant> getBpmnprof_participants() {
        return bpmnprof_participants;
    }

    public void addBpmnprof_participant(Bpmnprof_participant bpmnprof_participant) {
        this.bpmnprof_participants.add(bpmnprof_participant);
    }
    public bpmnprof_Class getBpmnprof_class() {
        return bpmnprof_class;
    }

    public void setBpmnprof_class(bpmnprof_Class bpmnprof_class) {
        this.bpmnprof_class = bpmnprof_class;
    }
    public bpmnprof_Participant getBpmnprof_participant() {
        return bpmnprof_participant;
    }

    public void setBpmnprof_participant(bpmnprof_Participant bpmnprof_participant) {
        this.bpmnprof_participant = bpmnprof_participant;
    }

}