





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Participant extends BaseElement, InteractionNode {






    private BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration;




    private BPMNProfile_ParticipantAssociation bpmnprofile_participantassociation;




    private BPMNProfile_PartnerRole bpmnprofile_partnerrole;




    private List<BPMNProfile_PartnerEntity> bpmnprofile_partnerentitys;




    private List<BPMNProfile_PartnerRole> bpmnprofile_partnerroles;




    private List<BPMNProfile_BPMNInterface> bpmnprofile_bpmninterfaces;




    private BPMNProfile_ConversationNode bpmnprofile_conversationnode;




    private BPMNProfile_PartnerEntity bpmnprofile_partnerentity;




    private BPMNProfile_ParticipantAssociation bpmnprofile_participantassociation;




    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;


    public BPMNProfile_Participant(
    ) {
        super(
        );
        this.bpmnprofile_partnerentitys = new ArrayList<>();
        this.bpmnprofile_partnerroles = new ArrayList<>();
        this.bpmnprofile_bpmninterfaces = new ArrayList<>();
    }

    public BPMNProfile_Participant(
        ArrayList<BPMNProfile_PartnerEntity> bpmnprofile_partnerentitys,        ArrayList<BPMNProfile_PartnerRole> bpmnprofile_partnerroles,        ArrayList<BPMNProfile_BPMNInterface> bpmnprofile_bpmninterfaces    ) {
        this.bpmnprofile_partnerentitys = bpmnprofile_partnerentitys;
        this.bpmnprofile_partnerroles = bpmnprofile_partnerroles;
        this.bpmnprofile_bpmninterfaces = bpmnprofile_bpmninterfaces;
    }


    public BPMNProfile_BPMNCollaboration getBpmnprofile_bpmncollaboration() {
        return bpmnprofile_bpmncollaboration;
    }

    public void setBpmnprofile_bpmncollaboration(BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration) {
        this.bpmnprofile_bpmncollaboration = bpmnprofile_bpmncollaboration;
    }
    public BPMNProfile_ParticipantAssociation getBpmnprofile_participantassociation() {
        return bpmnprofile_participantassociation;
    }

    public void setBpmnprofile_participantassociation(BPMNProfile_ParticipantAssociation bpmnprofile_participantassociation) {
        this.bpmnprofile_participantassociation = bpmnprofile_participantassociation;
    }
    public BPMNProfile_PartnerRole getBpmnprofile_partnerrole() {
        return bpmnprofile_partnerrole;
    }

    public void setBpmnprofile_partnerrole(BPMNProfile_PartnerRole bpmnprofile_partnerrole) {
        this.bpmnprofile_partnerrole = bpmnprofile_partnerrole;
    }
    public List<BPMNProfile_PartnerEntity> getBpmnprofile_partnerentitys() {
        return bpmnprofile_partnerentitys;
    }

    public void addBpmnprofile_partnerentity(Bpmnprofile_partnerentity bpmnprofile_partnerentity) {
        this.bpmnprofile_partnerentitys.add(bpmnprofile_partnerentity);
    }
    public List<BPMNProfile_PartnerRole> getBpmnprofile_partnerroles() {
        return bpmnprofile_partnerroles;
    }

    public void addBpmnprofile_partnerrole(Bpmnprofile_partnerrole bpmnprofile_partnerrole) {
        this.bpmnprofile_partnerroles.add(bpmnprofile_partnerrole);
    }
    public List<BPMNProfile_BPMNInterface> getBpmnprofile_bpmninterfaces() {
        return bpmnprofile_bpmninterfaces;
    }

    public void addBpmnprofile_bpmninterface(Bpmnprofile_bpmninterface bpmnprofile_bpmninterface) {
        this.bpmnprofile_bpmninterfaces.add(bpmnprofile_bpmninterface);
    }
    public BPMNProfile_ConversationNode getBpmnprofile_conversationnode() {
        return bpmnprofile_conversationnode;
    }

    public void setBpmnprofile_conversationnode(BPMNProfile_ConversationNode bpmnprofile_conversationnode) {
        this.bpmnprofile_conversationnode = bpmnprofile_conversationnode;
    }
    public BPMNProfile_PartnerEntity getBpmnprofile_partnerentity() {
        return bpmnprofile_partnerentity;
    }

    public void setBpmnprofile_partnerentity(BPMNProfile_PartnerEntity bpmnprofile_partnerentity) {
        this.bpmnprofile_partnerentity = bpmnprofile_partnerentity;
    }
    public BPMNProfile_ParticipantAssociation getBpmnprofile_participantassociation() {
        return bpmnprofile_participantassociation;
    }

    public void setBpmnprofile_participantassociation(BPMNProfile_ParticipantAssociation bpmnprofile_participantassociation) {
        this.bpmnprofile_participantassociation = bpmnprofile_participantassociation;
    }
    public BPMNProfile_BPMNProcess getBpmnprofile_bpmnprocess() {
        return bpmnprofile_bpmnprocess;
    }

    public void setBpmnprofile_bpmnprocess(BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess) {
        this.bpmnprofile_bpmnprocess = bpmnprofile_bpmnprocess;
    }

}