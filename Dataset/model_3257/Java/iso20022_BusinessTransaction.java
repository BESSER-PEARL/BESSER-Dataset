





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessTransaction extends TopLevelCatalogueEntry {






    private iso20022_Participant iso20022_participant;




    private iso20022_MessageChoreography iso20022_messagechoreography;




    private List<iso20022_MessageChoreography> iso20022_messagechoreographys;




    private List<iso20022_BusinessTransaction> iso20022_businesstransactions;




    private List<iso20022_MessageTransmission> iso20022_messagetransmissions;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_MessageTransmission iso20022_messagetransmission;




    private List<iso20022_Participant> iso20022_participants;


    public iso20022_BusinessTransaction(
    ) {
        super(
        );
        this.iso20022_messagechoreographys = new ArrayList<>();
        this.iso20022_businesstransactions = new ArrayList<>();
        this.iso20022_messagetransmissions = new ArrayList<>();
        this.iso20022_participants = new ArrayList<>();
    }

    public iso20022_BusinessTransaction(
        ArrayList<iso20022_MessageChoreography> iso20022_messagechoreographys,        ArrayList<iso20022_BusinessTransaction> iso20022_businesstransactions,        ArrayList<iso20022_MessageTransmission> iso20022_messagetransmissions,        ArrayList<iso20022_Participant> iso20022_participants    ) {
        this.iso20022_messagechoreographys = iso20022_messagechoreographys;
        this.iso20022_businesstransactions = iso20022_businesstransactions;
        this.iso20022_messagetransmissions = iso20022_messagetransmissions;
        this.iso20022_participants = iso20022_participants;
    }


    public iso20022_Participant getIso20022_participant() {
        return iso20022_participant;
    }

    public void setIso20022_participant(iso20022_Participant iso20022_participant) {
        this.iso20022_participant = iso20022_participant;
    }
    public iso20022_MessageChoreography getIso20022_messagechoreography() {
        return iso20022_messagechoreography;
    }

    public void setIso20022_messagechoreography(iso20022_MessageChoreography iso20022_messagechoreography) {
        this.iso20022_messagechoreography = iso20022_messagechoreography;
    }
    public List<iso20022_MessageChoreography> getIso20022_messagechoreographys() {
        return iso20022_messagechoreographys;
    }

    public void addIso20022_messagechoreography(Iso20022_messagechoreography iso20022_messagechoreography) {
        this.iso20022_messagechoreographys.add(iso20022_messagechoreography);
    }
    public List<iso20022_BusinessTransaction> getIso20022_businesstransactions() {
        return iso20022_businesstransactions;
    }

    public void addIso20022_businesstransaction(Iso20022_businesstransaction iso20022_businesstransaction) {
        this.iso20022_businesstransactions.add(iso20022_businesstransaction);
    }
    public List<iso20022_MessageTransmission> getIso20022_messagetransmissions() {
        return iso20022_messagetransmissions;
    }

    public void addIso20022_messagetransmission(Iso20022_messagetransmission iso20022_messagetransmission) {
        this.iso20022_messagetransmissions.add(iso20022_messagetransmission);
    }
    public iso20022_BusinessTransaction getIso20022_businesstransaction() {
        return iso20022_businesstransaction;
    }

    public void setIso20022_businesstransaction(iso20022_BusinessTransaction iso20022_businesstransaction) {
        this.iso20022_businesstransaction = iso20022_businesstransaction;
    }
    public iso20022_MessageTransmission getIso20022_messagetransmission() {
        return iso20022_messagetransmission;
    }

    public void setIso20022_messagetransmission(iso20022_MessageTransmission iso20022_messagetransmission) {
        this.iso20022_messagetransmission = iso20022_messagetransmission;
    }
    public List<iso20022_Participant> getIso20022_participants() {
        return iso20022_participants;
    }

    public void addIso20022_participant(Iso20022_participant iso20022_participant) {
        this.iso20022_participants.add(iso20022_participant);
    }

}