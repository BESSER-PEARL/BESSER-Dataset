





import java.util.List;
import java.util.ArrayList;

public class model_AssociationRelationship extends DependendencyRelationship {

    private boolean directed;



    public model_AssociationRelationship(
        boolean directed    ) {
        super(
        );
        this.directed = directed;
    }


    public boolean getDirected() {
        return directed;
    }

    public void setDirected(boolean directed) {
        this.directed = directed;
    }


}