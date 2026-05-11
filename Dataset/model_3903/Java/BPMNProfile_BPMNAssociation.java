





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNAssociation extends BPMNArtifact {

    private String associationDirection;



    public BPMNProfile_BPMNAssociation(
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