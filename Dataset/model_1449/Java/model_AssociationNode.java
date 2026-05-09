





import java.util.List;
import java.util.ArrayList;

public class model_AssociationNode extends Node {

    private String associationTypeConstraint;



    public model_AssociationNode(
        String associationTypeConstraint    ) {
        super(
        );
        this.associationTypeConstraint = associationTypeConstraint;
    }


    public String getAssociationtypeconstraint() {
        return associationTypeConstraint;
    }

    public void setAssociationtypeconstraint(String associationTypeConstraint) {
        this.associationTypeConstraint = associationTypeConstraint;
    }


}