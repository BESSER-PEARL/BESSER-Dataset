





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Collaboration extends RootElement {

    private boolean isClosed;
    private String name;





    private List<bpmn2_ParticipantAssociation> bpmn2_participantassociations;




    private List<bpmn2_Artifact> bpmn2_artifacts;




    private List<bpmn2_ConversationNode> bpmn2_conversationnodes;




    private List<bpmn2_MessageFlow> bpmn2_messageflows;




    private List<bpmn2_Participant> bpmn2_participants;




    private bpmn2_ConversationAssociation bpmn2_conversationassociation;




    private List<bpmn2_CorrelationKey> bpmn2_correlationkeys;




    private List<bpmn2_MessageFlowAssociation> bpmn2_messageflowassociations;




    private List<bpmn2_ConversationLink> bpmn2_conversationlinks;


    public bpmn2_Collaboration(
        boolean isClosed,        String name    ) {
        super(
        );
        this.isClosed = isClosed;
        this.name = name;
        this.bpmn2_participantassociations = new ArrayList<>();
        this.bpmn2_artifacts = new ArrayList<>();
        this.bpmn2_conversationnodes = new ArrayList<>();
        this.bpmn2_messageflows = new ArrayList<>();
        this.bpmn2_participants = new ArrayList<>();
        this.bpmn2_correlationkeys = new ArrayList<>();
        this.bpmn2_messageflowassociations = new ArrayList<>();
        this.bpmn2_conversationlinks = new ArrayList<>();
    }

    public bpmn2_Collaboration(
        boolean isClosed,        String name        ArrayList<bpmn2_ParticipantAssociation> bpmn2_participantassociations,        ArrayList<bpmn2_Artifact> bpmn2_artifacts,        ArrayList<bpmn2_ConversationNode> bpmn2_conversationnodes,        ArrayList<bpmn2_MessageFlow> bpmn2_messageflows,        ArrayList<bpmn2_Participant> bpmn2_participants,        ArrayList<bpmn2_CorrelationKey> bpmn2_correlationkeys,        ArrayList<bpmn2_MessageFlowAssociation> bpmn2_messageflowassociations,        ArrayList<bpmn2_ConversationLink> bpmn2_conversationlinks    ) {
        this.isClosed = isClosed;
        this.name = name;
        this.bpmn2_participantassociations = bpmn2_participantassociations;
        this.bpmn2_artifacts = bpmn2_artifacts;
        this.bpmn2_conversationnodes = bpmn2_conversationnodes;
        this.bpmn2_messageflows = bpmn2_messageflows;
        this.bpmn2_participants = bpmn2_participants;
        this.bpmn2_correlationkeys = bpmn2_correlationkeys;
        this.bpmn2_messageflowassociations = bpmn2_messageflowassociations;
        this.bpmn2_conversationlinks = bpmn2_conversationlinks;
    }

    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_ParticipantAssociation> getBpmn2_participantassociations() {
        return bpmn2_participantassociations;
    }

    public void addBpmn2_participantassociation(Bpmn2_participantassociation bpmn2_participantassociation) {
        this.bpmn2_participantassociations.add(bpmn2_participantassociation);
    }
    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }
    public List<bpmn2_ConversationNode> getBpmn2_conversationnodes() {
        return bpmn2_conversationnodes;
    }

    public void addBpmn2_conversationnode(Bpmn2_conversationnode bpmn2_conversationnode) {
        this.bpmn2_conversationnodes.add(bpmn2_conversationnode);
    }
    public List<bpmn2_MessageFlow> getBpmn2_messageflows() {
        return bpmn2_messageflows;
    }

    public void addBpmn2_messageflow(Bpmn2_messageflow bpmn2_messageflow) {
        this.bpmn2_messageflows.add(bpmn2_messageflow);
    }
    public List<bpmn2_Participant> getBpmn2_participants() {
        return bpmn2_participants;
    }

    public void addBpmn2_participant(Bpmn2_participant bpmn2_participant) {
        this.bpmn2_participants.add(bpmn2_participant);
    }
    public bpmn2_ConversationAssociation getBpmn2_conversationassociation() {
        return bpmn2_conversationassociation;
    }

    public void setBpmn2_conversationassociation(bpmn2_ConversationAssociation bpmn2_conversationassociation) {
        this.bpmn2_conversationassociation = bpmn2_conversationassociation;
    }
    public List<bpmn2_CorrelationKey> getBpmn2_correlationkeys() {
        return bpmn2_correlationkeys;
    }

    public void addBpmn2_correlationkey(Bpmn2_correlationkey bpmn2_correlationkey) {
        this.bpmn2_correlationkeys.add(bpmn2_correlationkey);
    }
    public List<bpmn2_MessageFlowAssociation> getBpmn2_messageflowassociations() {
        return bpmn2_messageflowassociations;
    }

    public void addBpmn2_messageflowassociation(Bpmn2_messageflowassociation bpmn2_messageflowassociation) {
        this.bpmn2_messageflowassociations.add(bpmn2_messageflowassociation);
    }
    public List<bpmn2_ConversationLink> getBpmn2_conversationlinks() {
        return bpmn2_conversationlinks;
    }

    public void addBpmn2_conversationlink(Bpmn2_conversationlink bpmn2_conversationlink) {
        this.bpmn2_conversationlinks.add(bpmn2_conversationlink);
    }

}