





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Collaboration extends RootElement {

    private String name;
    private boolean isClosed;





    private BPMN2Model_ConversationAssociation bpmn2model_conversationassociation;




    private BPMN2Model_Process bpmn2model_process;




    private List<BPMN2Model_Artifact> bpmn2model_artifacts;




    private List<BPMN2Model_CorrelationKey> bpmn2model_correlationkeys;




    private List<BPMN2Model_ConversationLink> bpmn2model_conversationlinks;




    private List<BPMN2Model_MessageFlowAssociation> bpmn2model_messageflowassociations;




    private List<BPMN2Model_Participant> bpmn2model_participants;




    private List<BPMN2Model_ConversationNode> bpmn2model_conversationnodes;




    private List<BPMN2Model_MessageFlow> bpmn2model_messageflows;




    private List<BPMN2Model_ParticipantAssociation> bpmn2model_participantassociations;




    private BPMN2Model_CallConversation bpmn2model_callconversation;


    public BPMN2Model_Collaboration(
        String name,        boolean isClosed    ) {
        super(
        );
        this.name = name;
        this.isClosed = isClosed;
        this.bpmn2model_artifacts = new ArrayList<>();
        this.bpmn2model_correlationkeys = new ArrayList<>();
        this.bpmn2model_conversationlinks = new ArrayList<>();
        this.bpmn2model_messageflowassociations = new ArrayList<>();
        this.bpmn2model_participants = new ArrayList<>();
        this.bpmn2model_conversationnodes = new ArrayList<>();
        this.bpmn2model_messageflows = new ArrayList<>();
        this.bpmn2model_participantassociations = new ArrayList<>();
    }

    public BPMN2Model_Collaboration(
        String name,        boolean isClosed        ArrayList<BPMN2Model_Artifact> bpmn2model_artifacts,        ArrayList<BPMN2Model_CorrelationKey> bpmn2model_correlationkeys,        ArrayList<BPMN2Model_ConversationLink> bpmn2model_conversationlinks,        ArrayList<BPMN2Model_MessageFlowAssociation> bpmn2model_messageflowassociations,        ArrayList<BPMN2Model_Participant> bpmn2model_participants,        ArrayList<BPMN2Model_ConversationNode> bpmn2model_conversationnodes,        ArrayList<BPMN2Model_MessageFlow> bpmn2model_messageflows,        ArrayList<BPMN2Model_ParticipantAssociation> bpmn2model_participantassociations    ) {
        this.name = name;
        this.isClosed = isClosed;
        this.bpmn2model_artifacts = bpmn2model_artifacts;
        this.bpmn2model_correlationkeys = bpmn2model_correlationkeys;
        this.bpmn2model_conversationlinks = bpmn2model_conversationlinks;
        this.bpmn2model_messageflowassociations = bpmn2model_messageflowassociations;
        this.bpmn2model_participants = bpmn2model_participants;
        this.bpmn2model_conversationnodes = bpmn2model_conversationnodes;
        this.bpmn2model_messageflows = bpmn2model_messageflows;
        this.bpmn2model_participantassociations = bpmn2model_participantassociations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }

    public BPMN2Model_ConversationAssociation getBpmn2model_conversationassociation() {
        return bpmn2model_conversationassociation;
    }

    public void setBpmn2model_conversationassociation(BPMN2Model_ConversationAssociation bpmn2model_conversationassociation) {
        this.bpmn2model_conversationassociation = bpmn2model_conversationassociation;
    }
    public BPMN2Model_Process getBpmn2model_process() {
        return bpmn2model_process;
    }

    public void setBpmn2model_process(BPMN2Model_Process bpmn2model_process) {
        this.bpmn2model_process = bpmn2model_process;
    }
    public List<BPMN2Model_Artifact> getBpmn2model_artifacts() {
        return bpmn2model_artifacts;
    }

    public void addBpmn2model_artifact(Bpmn2model_artifact bpmn2model_artifact) {
        this.bpmn2model_artifacts.add(bpmn2model_artifact);
    }
    public List<BPMN2Model_CorrelationKey> getBpmn2model_correlationkeys() {
        return bpmn2model_correlationkeys;
    }

    public void addBpmn2model_correlationkey(Bpmn2model_correlationkey bpmn2model_correlationkey) {
        this.bpmn2model_correlationkeys.add(bpmn2model_correlationkey);
    }
    public List<BPMN2Model_ConversationLink> getBpmn2model_conversationlinks() {
        return bpmn2model_conversationlinks;
    }

    public void addBpmn2model_conversationlink(Bpmn2model_conversationlink bpmn2model_conversationlink) {
        this.bpmn2model_conversationlinks.add(bpmn2model_conversationlink);
    }
    public List<BPMN2Model_MessageFlowAssociation> getBpmn2model_messageflowassociations() {
        return bpmn2model_messageflowassociations;
    }

    public void addBpmn2model_messageflowassociation(Bpmn2model_messageflowassociation bpmn2model_messageflowassociation) {
        this.bpmn2model_messageflowassociations.add(bpmn2model_messageflowassociation);
    }
    public List<BPMN2Model_Participant> getBpmn2model_participants() {
        return bpmn2model_participants;
    }

    public void addBpmn2model_participant(Bpmn2model_participant bpmn2model_participant) {
        this.bpmn2model_participants.add(bpmn2model_participant);
    }
    public List<BPMN2Model_ConversationNode> getBpmn2model_conversationnodes() {
        return bpmn2model_conversationnodes;
    }

    public void addBpmn2model_conversationnode(Bpmn2model_conversationnode bpmn2model_conversationnode) {
        this.bpmn2model_conversationnodes.add(bpmn2model_conversationnode);
    }
    public List<BPMN2Model_MessageFlow> getBpmn2model_messageflows() {
        return bpmn2model_messageflows;
    }

    public void addBpmn2model_messageflow(Bpmn2model_messageflow bpmn2model_messageflow) {
        this.bpmn2model_messageflows.add(bpmn2model_messageflow);
    }
    public List<BPMN2Model_ParticipantAssociation> getBpmn2model_participantassociations() {
        return bpmn2model_participantassociations;
    }

    public void addBpmn2model_participantassociation(Bpmn2model_participantassociation bpmn2model_participantassociation) {
        this.bpmn2model_participantassociations.add(bpmn2model_participantassociation);
    }
    public BPMN2Model_CallConversation getBpmn2model_callconversation() {
        return bpmn2model_callconversation;
    }

    public void setBpmn2model_callconversation(BPMN2Model_CallConversation bpmn2model_callconversation) {
        this.bpmn2model_callconversation = bpmn2model_callconversation;
    }

}