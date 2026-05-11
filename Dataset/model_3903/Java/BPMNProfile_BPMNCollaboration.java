





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNCollaboration extends RootElement {

    private String isClosed;





    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;




    private List<BPMNProfile_ConversationLink> bpmnprofile_conversationlinks;




    private List<BPMNProfile_ParticipantAssociation> bpmnprofile_participantassociations;




    private List<BPMNProfile_Participant> bpmnprofile_participants;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_CallConversation bpmnprofile_callconversation;




    private List<BPMNProfile_CorrelationKey> bpmnprofile_correlationkeys;




    private List<BPMNProfile_MessageFlowAssociation> bpmnprofile_messageflowassociations;




    private List<BPMNProfile_MessageFlow> bpmnprofile_messageflows;


    public BPMNProfile_BPMNCollaboration(
        String isClosed    ) {
        super(
        );
        this.isClosed = isClosed;
        this.bpmnprofile_conversationlinks = new ArrayList<>();
        this.bpmnprofile_participantassociations = new ArrayList<>();
        this.bpmnprofile_participants = new ArrayList<>();
        this.bpmnprofile_correlationkeys = new ArrayList<>();
        this.bpmnprofile_messageflowassociations = new ArrayList<>();
        this.bpmnprofile_messageflows = new ArrayList<>();
    }

    public BPMNProfile_BPMNCollaboration(
        String isClosed        ArrayList<BPMNProfile_ConversationLink> bpmnprofile_conversationlinks,        ArrayList<BPMNProfile_ParticipantAssociation> bpmnprofile_participantassociations,        ArrayList<BPMNProfile_Participant> bpmnprofile_participants,        ArrayList<BPMNProfile_CorrelationKey> bpmnprofile_correlationkeys,        ArrayList<BPMNProfile_MessageFlowAssociation> bpmnprofile_messageflowassociations,        ArrayList<BPMNProfile_MessageFlow> bpmnprofile_messageflows    ) {
        this.isClosed = isClosed;
        this.bpmnprofile_conversationlinks = bpmnprofile_conversationlinks;
        this.bpmnprofile_participantassociations = bpmnprofile_participantassociations;
        this.bpmnprofile_participants = bpmnprofile_participants;
        this.bpmnprofile_correlationkeys = bpmnprofile_correlationkeys;
        this.bpmnprofile_messageflowassociations = bpmnprofile_messageflowassociations;
        this.bpmnprofile_messageflows = bpmnprofile_messageflows;
    }

    public String getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(String isClosed) {
        this.isClosed = isClosed;
    }

    public BPMNProfile_BPMNProcess getBpmnprofile_bpmnprocess() {
        return bpmnprofile_bpmnprocess;
    }

    public void setBpmnprofile_bpmnprocess(BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess) {
        this.bpmnprofile_bpmnprocess = bpmnprofile_bpmnprocess;
    }
    public List<BPMNProfile_ConversationLink> getBpmnprofile_conversationlinks() {
        return bpmnprofile_conversationlinks;
    }

    public void addBpmnprofile_conversationlink(Bpmnprofile_conversationlink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlinks.add(bpmnprofile_conversationlink);
    }
    public List<BPMNProfile_ParticipantAssociation> getBpmnprofile_participantassociations() {
        return bpmnprofile_participantassociations;
    }

    public void addBpmnprofile_participantassociation(Bpmnprofile_participantassociation bpmnprofile_participantassociation) {
        this.bpmnprofile_participantassociations.add(bpmnprofile_participantassociation);
    }
    public List<BPMNProfile_Participant> getBpmnprofile_participants() {
        return bpmnprofile_participants;
    }

    public void addBpmnprofile_participant(Bpmnprofile_participant bpmnprofile_participant) {
        this.bpmnprofile_participants.add(bpmnprofile_participant);
    }
    public BPMNProfile_ConversationLink getBpmnprofile_conversationlink() {
        return bpmnprofile_conversationlink;
    }

    public void setBpmnprofile_conversationlink(BPMNProfile_ConversationLink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlink = bpmnprofile_conversationlink;
    }
    public BPMNProfile_CallConversation getBpmnprofile_callconversation() {
        return bpmnprofile_callconversation;
    }

    public void setBpmnprofile_callconversation(BPMNProfile_CallConversation bpmnprofile_callconversation) {
        this.bpmnprofile_callconversation = bpmnprofile_callconversation;
    }
    public List<BPMNProfile_CorrelationKey> getBpmnprofile_correlationkeys() {
        return bpmnprofile_correlationkeys;
    }

    public void addBpmnprofile_correlationkey(Bpmnprofile_correlationkey bpmnprofile_correlationkey) {
        this.bpmnprofile_correlationkeys.add(bpmnprofile_correlationkey);
    }
    public List<BPMNProfile_MessageFlowAssociation> getBpmnprofile_messageflowassociations() {
        return bpmnprofile_messageflowassociations;
    }

    public void addBpmnprofile_messageflowassociation(Bpmnprofile_messageflowassociation bpmnprofile_messageflowassociation) {
        this.bpmnprofile_messageflowassociations.add(bpmnprofile_messageflowassociation);
    }
    public List<BPMNProfile_MessageFlow> getBpmnprofile_messageflows() {
        return bpmnprofile_messageflows;
    }

    public void addBpmnprofile_messageflow(Bpmnprofile_messageflow bpmnprofile_messageflow) {
        this.bpmnprofile_messageflows.add(bpmnprofile_messageflow);
    }

}