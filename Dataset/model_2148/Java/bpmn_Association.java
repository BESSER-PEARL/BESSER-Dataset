





import java.util.List;
import java.util.ArrayList;

public class bpmn_Association extends EModelElement {

    private String direction;





    private bpmn_Artifact bpmn_artifact;




    private bpmn_Artifact bpmn_artifact;




    private bpmn_AssociationTarget bpmn_associationtarget;




    private bpmn_AssociationTarget bpmn_associationtarget;


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
    public bpmn_Artifact getBpmn_artifact() {
        return bpmn_artifact;
    }

    public void setBpmn_artifact(bpmn_Artifact bpmn_artifact) {
        this.bpmn_artifact = bpmn_artifact;
    }
    public bpmn_AssociationTarget getBpmn_associationtarget() {
        return bpmn_associationtarget;
    }

    public void setBpmn_associationtarget(bpmn_AssociationTarget bpmn_associationtarget) {
        this.bpmn_associationtarget = bpmn_associationtarget;
    }
    public bpmn_AssociationTarget getBpmn_associationtarget() {
        return bpmn_associationtarget;
    }

    public void setBpmn_associationtarget(bpmn_AssociationTarget bpmn_associationtarget) {
        this.bpmn_associationtarget = bpmn_associationtarget;
    }

}