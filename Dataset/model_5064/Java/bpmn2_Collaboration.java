





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Collaboration extends RootElement {

    private boolean isClosed;





    private List<bpmn2_ConversationNode> bpmn2_conversationnodes;




    private List<bpmn2_Artifact> bpmn2_artifacts;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_CallConversation bpmn2_callconversation;




    private List<bpmn2_Choreography> bpmn2_choreographys;


    public bpmn2_Collaboration(
        boolean isClosed    ) {
        super(
        );
        this.isClosed = isClosed;
        this.bpmn2_conversationnodes = new ArrayList<>();
        this.bpmn2_artifacts = new ArrayList<>();
        this.bpmn2_choreographys = new ArrayList<>();
    }

    public bpmn2_Collaboration(
        boolean isClosed        ArrayList<bpmn2_ConversationNode> bpmn2_conversationnodes,        ArrayList<bpmn2_Artifact> bpmn2_artifacts,        ArrayList<bpmn2_Choreography> bpmn2_choreographys    ) {
        this.isClosed = isClosed;
        this.bpmn2_conversationnodes = bpmn2_conversationnodes;
        this.bpmn2_artifacts = bpmn2_artifacts;
        this.bpmn2_choreographys = bpmn2_choreographys;
    }

    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }

    public List<bpmn2_ConversationNode> getBpmn2_conversationnodes() {
        return bpmn2_conversationnodes;
    }

    public void addBpmn2_conversationnode(Bpmn2_conversationnode bpmn2_conversationnode) {
        this.bpmn2_conversationnodes.add(bpmn2_conversationnode);
    }
    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_CallConversation getBpmn2_callconversation() {
        return bpmn2_callconversation;
    }

    public void setBpmn2_callconversation(bpmn2_CallConversation bpmn2_callconversation) {
        this.bpmn2_callconversation = bpmn2_callconversation;
    }
    public List<bpmn2_Choreography> getBpmn2_choreographys() {
        return bpmn2_choreographys;
    }

    public void addBpmn2_choreography(Bpmn2_choreography bpmn2_choreography) {
        this.bpmn2_choreographys.add(bpmn2_choreography);
    }

}