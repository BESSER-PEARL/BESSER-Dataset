





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNCollaboration extends RootElement {

    private String isClosed;





    private List<bpmnprof_ConversationLink> bpmnprof_conversationlinks;




    private bpmnprof_ConversationLink bpmnprof_conversationlink;




    private List<bpmnprof_Participant> bpmnprof_participants;




    private bpmnprof_BPMNProcess bpmnprof_bpmnprocess;




    private List<bpmnprof_CorrelationKey> bpmnprof_correlationkeys;




    private List<bpmnprof_MessageFlow> bpmnprof_messageflows;




    private List<bpmnprof_ParticipantAssociation> bpmnprof_participantassociations;




    private List<bpmnprof_MessageFlowAssociation> bpmnprof_messageflowassociations;


    public bpmnprof_BPMNCollaboration(
        String isClosed    ) {
        super(
        );
        this.isClosed = isClosed;
        this.bpmnprof_conversationlinks = new ArrayList<>();
        this.bpmnprof_participants = new ArrayList<>();
        this.bpmnprof_correlationkeys = new ArrayList<>();
        this.bpmnprof_messageflows = new ArrayList<>();
        this.bpmnprof_participantassociations = new ArrayList<>();
        this.bpmnprof_messageflowassociations = new ArrayList<>();
    }

    public bpmnprof_BPMNCollaboration(
        String isClosed        ArrayList<bpmnprof_ConversationLink> bpmnprof_conversationlinks,        ArrayList<bpmnprof_Participant> bpmnprof_participants,        ArrayList<bpmnprof_CorrelationKey> bpmnprof_correlationkeys,        ArrayList<bpmnprof_MessageFlow> bpmnprof_messageflows,        ArrayList<bpmnprof_ParticipantAssociation> bpmnprof_participantassociations,        ArrayList<bpmnprof_MessageFlowAssociation> bpmnprof_messageflowassociations    ) {
        this.isClosed = isClosed;
        this.bpmnprof_conversationlinks = bpmnprof_conversationlinks;
        this.bpmnprof_participants = bpmnprof_participants;
        this.bpmnprof_correlationkeys = bpmnprof_correlationkeys;
        this.bpmnprof_messageflows = bpmnprof_messageflows;
        this.bpmnprof_participantassociations = bpmnprof_participantassociations;
        this.bpmnprof_messageflowassociations = bpmnprof_messageflowassociations;
    }

    public String getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(String isClosed) {
        this.isClosed = isClosed;
    }

    public List<bpmnprof_ConversationLink> getBpmnprof_conversationlinks() {
        return bpmnprof_conversationlinks;
    }

    public void addBpmnprof_conversationlink(Bpmnprof_conversationlink bpmnprof_conversationlink) {
        this.bpmnprof_conversationlinks.add(bpmnprof_conversationlink);
    }
    public bpmnprof_ConversationLink getBpmnprof_conversationlink() {
        return bpmnprof_conversationlink;
    }

    public void setBpmnprof_conversationlink(bpmnprof_ConversationLink bpmnprof_conversationlink) {
        this.bpmnprof_conversationlink = bpmnprof_conversationlink;
    }
    public List<bpmnprof_Participant> getBpmnprof_participants() {
        return bpmnprof_participants;
    }

    public void addBpmnprof_participant(Bpmnprof_participant bpmnprof_participant) {
        this.bpmnprof_participants.add(bpmnprof_participant);
    }
    public bpmnprof_BPMNProcess getBpmnprof_bpmnprocess() {
        return bpmnprof_bpmnprocess;
    }

    public void setBpmnprof_bpmnprocess(bpmnprof_BPMNProcess bpmnprof_bpmnprocess) {
        this.bpmnprof_bpmnprocess = bpmnprof_bpmnprocess;
    }
    public List<bpmnprof_CorrelationKey> getBpmnprof_correlationkeys() {
        return bpmnprof_correlationkeys;
    }

    public void addBpmnprof_correlationkey(Bpmnprof_correlationkey bpmnprof_correlationkey) {
        this.bpmnprof_correlationkeys.add(bpmnprof_correlationkey);
    }
    public List<bpmnprof_MessageFlow> getBpmnprof_messageflows() {
        return bpmnprof_messageflows;
    }

    public void addBpmnprof_messageflow(Bpmnprof_messageflow bpmnprof_messageflow) {
        this.bpmnprof_messageflows.add(bpmnprof_messageflow);
    }
    public List<bpmnprof_ParticipantAssociation> getBpmnprof_participantassociations() {
        return bpmnprof_participantassociations;
    }

    public void addBpmnprof_participantassociation(Bpmnprof_participantassociation bpmnprof_participantassociation) {
        this.bpmnprof_participantassociations.add(bpmnprof_participantassociation);
    }
    public List<bpmnprof_MessageFlowAssociation> getBpmnprof_messageflowassociations() {
        return bpmnprof_messageflowassociations;
    }

    public void addBpmnprof_messageflowassociation(Bpmnprof_messageflowassociation bpmnprof_messageflowassociation) {
        this.bpmnprof_messageflowassociations.add(bpmnprof_messageflowassociation);
    }

}