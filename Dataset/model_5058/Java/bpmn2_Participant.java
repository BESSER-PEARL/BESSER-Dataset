





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Participant extends BaseElement, InteractionNode {

    private String name;





    private bpmn2_ParticipantAssociation bpmn2_participantassociation;




    private bpmn2_PartnerEntity bpmn2_partnerentity;




    private bpmn2_ConversationNode bpmn2_conversationnode;




    private bpmn2_PartnerRole bpmn2_partnerrole;




    private bpmn2_Collaboration bpmn2_collaboration;




    private List<bpmn2_Interface> bpmn2_interfaces;




    private List<bpmn2_EndPoint> bpmn2_endpoints;




    private bpmn2_ParticipantAssociation bpmn2_participantassociation;


    public bpmn2_Participant(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_interfaces = new ArrayList<>();
        this.bpmn2_endpoints = new ArrayList<>();
    }

    public bpmn2_Participant(
        String name        ArrayList<bpmn2_Interface> bpmn2_interfaces,        ArrayList<bpmn2_EndPoint> bpmn2_endpoints    ) {
        this.name = name;
        this.bpmn2_interfaces = bpmn2_interfaces;
        this.bpmn2_endpoints = bpmn2_endpoints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ParticipantAssociation getBpmn2_participantassociation() {
        return bpmn2_participantassociation;
    }

    public void setBpmn2_participantassociation(bpmn2_ParticipantAssociation bpmn2_participantassociation) {
        this.bpmn2_participantassociation = bpmn2_participantassociation;
    }
    public bpmn2_PartnerEntity getBpmn2_partnerentity() {
        return bpmn2_partnerentity;
    }

    public void setBpmn2_partnerentity(bpmn2_PartnerEntity bpmn2_partnerentity) {
        this.bpmn2_partnerentity = bpmn2_partnerentity;
    }
    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }
    public bpmn2_PartnerRole getBpmn2_partnerrole() {
        return bpmn2_partnerrole;
    }

    public void setBpmn2_partnerrole(bpmn2_PartnerRole bpmn2_partnerrole) {
        this.bpmn2_partnerrole = bpmn2_partnerrole;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public List<bpmn2_Interface> getBpmn2_interfaces() {
        return bpmn2_interfaces;
    }

    public void addBpmn2_interface(Bpmn2_interface bpmn2_interface) {
        this.bpmn2_interfaces.add(bpmn2_interface);
    }
    public List<bpmn2_EndPoint> getBpmn2_endpoints() {
        return bpmn2_endpoints;
    }

    public void addBpmn2_endpoint(Bpmn2_endpoint bpmn2_endpoint) {
        this.bpmn2_endpoints.add(bpmn2_endpoint);
    }
    public bpmn2_ParticipantAssociation getBpmn2_participantassociation() {
        return bpmn2_participantassociation;
    }

    public void setBpmn2_participantassociation(bpmn2_ParticipantAssociation bpmn2_participantassociation) {
        this.bpmn2_participantassociation = bpmn2_participantassociation;
    }

}