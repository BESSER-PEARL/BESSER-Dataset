





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Participant extends BaseElement, InteractionNode {






    private List<bpmn2_EndPoint> bpmn2_endpoints;




    private bpmn2_ConversationNode bpmn2_conversationnode;




    private bpmn2_ChoreographyActivity bpmn2_choreographyactivity;




    private List<bpmn2_Interface> bpmn2_interfaces;




    private bpmn2_GlobalChoreographyTask bpmn2_globalchoreographytask;




    private bpmn2_ChoreographyActivity bpmn2_choreographyactivity;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Collaboration bpmn2_collaboration;


    public bpmn2_Participant(
    ) {
        super(
        );
        this.bpmn2_endpoints = new ArrayList<>();
        this.bpmn2_interfaces = new ArrayList<>();
    }

    public bpmn2_Participant(
        ArrayList<bpmn2_EndPoint> bpmn2_endpoints,        ArrayList<bpmn2_Interface> bpmn2_interfaces    ) {
        this.bpmn2_endpoints = bpmn2_endpoints;
        this.bpmn2_interfaces = bpmn2_interfaces;
    }


    public List<bpmn2_EndPoint> getBpmn2_endpoints() {
        return bpmn2_endpoints;
    }

    public void addBpmn2_endpoint(Bpmn2_endpoint bpmn2_endpoint) {
        this.bpmn2_endpoints.add(bpmn2_endpoint);
    }
    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }
    public bpmn2_ChoreographyActivity getBpmn2_choreographyactivity() {
        return bpmn2_choreographyactivity;
    }

    public void setBpmn2_choreographyactivity(bpmn2_ChoreographyActivity bpmn2_choreographyactivity) {
        this.bpmn2_choreographyactivity = bpmn2_choreographyactivity;
    }
    public List<bpmn2_Interface> getBpmn2_interfaces() {
        return bpmn2_interfaces;
    }

    public void addBpmn2_interface(Bpmn2_interface bpmn2_interface) {
        this.bpmn2_interfaces.add(bpmn2_interface);
    }
    public bpmn2_GlobalChoreographyTask getBpmn2_globalchoreographytask() {
        return bpmn2_globalchoreographytask;
    }

    public void setBpmn2_globalchoreographytask(bpmn2_GlobalChoreographyTask bpmn2_globalchoreographytask) {
        this.bpmn2_globalchoreographytask = bpmn2_globalchoreographytask;
    }
    public bpmn2_ChoreographyActivity getBpmn2_choreographyactivity() {
        return bpmn2_choreographyactivity;
    }

    public void setBpmn2_choreographyactivity(bpmn2_ChoreographyActivity bpmn2_choreographyactivity) {
        this.bpmn2_choreographyactivity = bpmn2_choreographyactivity;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }

}