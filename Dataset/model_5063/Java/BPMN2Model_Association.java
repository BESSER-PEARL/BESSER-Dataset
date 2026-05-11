





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Association extends Artifact {

    private String associationDirection;



    public BPMN2Model_Association(
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