





import java.util.List;
import java.util.ArrayList;

public class gremlin_OutEStep extends Step {

    private String relationshipName;



    public gremlin_OutEStep(
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