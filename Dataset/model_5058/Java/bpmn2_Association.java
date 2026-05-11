





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Association extends Artifact {

    private String associationDirection;





    private bpmn2_BaseElement bpmn2_baseelement;




    private bpmn2_BaseElement bpmn2_baseelement;


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

    public bpmn2_BaseElement getBpmn2_baseelement() {
        return bpmn2_baseelement;
    }

    public void setBpmn2_baseelement(bpmn2_BaseElement bpmn2_baseelement) {
        this.bpmn2_baseelement = bpmn2_baseelement;
    }
    public bpmn2_BaseElement getBpmn2_baseelement() {
        return bpmn2_baseelement;
    }

    public void setBpmn2_baseelement(bpmn2_BaseElement bpmn2_baseelement) {
        this.bpmn2_baseelement = bpmn2_baseelement;
    }

}