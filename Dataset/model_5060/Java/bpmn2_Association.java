





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Association extends Artifact {

    private String associationDirection;



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


}