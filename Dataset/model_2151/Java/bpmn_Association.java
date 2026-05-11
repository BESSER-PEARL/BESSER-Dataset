





import java.util.List;
import java.util.ArrayList;

public class bpmn_Association extends EModelElement {

    private String direction;





    private bpmn_Artifact bpmn_artifact;




    private bpmn_IdentifiableNode bpmn_identifiablenode;




    private bpmn_IdentifiableNode bpmn_identifiablenode;




    private bpmn_Artifact bpmn_artifact;


    public bpmn_Association(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public bpmn_Artifact getBpmn_artifact() {
        return bpmn_artifact;
    }

    public void setBpmn_artifact(bpmn_Artifact bpmn_artifact) {
        this.bpmn_artifact = bpmn_artifact;
    }
    public bpmn_IdentifiableNode getBpmn_identifiablenode() {
        return bpmn_identifiablenode;
    }

    public void setBpmn_identifiablenode(bpmn_IdentifiableNode bpmn_identifiablenode) {
        this.bpmn_identifiablenode = bpmn_identifiablenode;
    }
    public bpmn_IdentifiableNode getBpmn_identifiablenode() {
        return bpmn_identifiablenode;
    }

    public void setBpmn_identifiablenode(bpmn_IdentifiableNode bpmn_identifiablenode) {
        this.bpmn_identifiablenode = bpmn_identifiablenode;
    }
    public bpmn_Artifact getBpmn_artifact() {
        return bpmn_artifact;
    }

    public void setBpmn_artifact(bpmn_Artifact bpmn_artifact) {
        this.bpmn_artifact = bpmn_artifact;
    }

}