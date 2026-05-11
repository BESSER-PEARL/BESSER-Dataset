





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessRole extends RepositoryConcept {






    private iso20022_BusinessProcess iso20022_businessprocess;




    private iso20022_BusinessProcess iso20022_businessprocess;




    private iso20022_Participant iso20022_participant;




    private List<iso20022_Participant> iso20022_participants;


    public iso20022_BusinessRole(
    ) {
        super(
        );
        this.iso20022_participants = new ArrayList<>();
    }

    public iso20022_BusinessRole(
        ArrayList<iso20022_Participant> iso20022_participants    ) {
        this.iso20022_participants = iso20022_participants;
    }


    public iso20022_BusinessProcess getIso20022_businessprocess() {
        return iso20022_businessprocess;
    }

    public void setIso20022_businessprocess(iso20022_BusinessProcess iso20022_businessprocess) {
        this.iso20022_businessprocess = iso20022_businessprocess;
    }
    public iso20022_BusinessProcess getIso20022_businessprocess() {
        return iso20022_businessprocess;
    }

    public void setIso20022_businessprocess(iso20022_BusinessProcess iso20022_businessprocess) {
        this.iso20022_businessprocess = iso20022_businessprocess;
    }
    public iso20022_Participant getIso20022_participant() {
        return iso20022_participant;
    }

    public void setIso20022_participant(iso20022_Participant iso20022_participant) {
        this.iso20022_participant = iso20022_participant;
    }
    public List<iso20022_Participant> getIso20022_participants() {
        return iso20022_participants;
    }

    public void addIso20022_participant(Iso20022_participant iso20022_participant) {
        this.iso20022_participants.add(iso20022_participant);
    }

}