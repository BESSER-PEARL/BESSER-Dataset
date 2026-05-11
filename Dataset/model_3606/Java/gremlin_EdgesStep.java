





import java.util.List;
import java.util.ArrayList;

public class gremlin_EdgesStep extends Step {

    private String relationshipName;



    public gremlin_EdgesStep(
        String relationshipName    ) {
        super(
        );
        this.relationshipName = relationshipName;
    }


    public String getRelationshipname() {
        return relationshipName;
    }

    public void setRelationshipname(String relationshipName) {
        this.relationshipName = relationshipName;
    }


}