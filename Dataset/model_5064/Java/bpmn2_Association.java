





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Association extends Artifact {

    private String associationDirection;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Association(
        String associationDirection    ) {
        super(
        );
        this.associationDirection = associationDirection;
    }


    public String getAssociationdirection() {
        return associationDirection;
    }

    public void setAssociationdirection(String associationDirection) {
        this.associationDirection = associationDirection;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}