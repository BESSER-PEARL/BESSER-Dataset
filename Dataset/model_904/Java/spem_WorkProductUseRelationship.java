





import java.util.List;
import java.util.ArrayList;

public class spem_WorkProductUseRelationship extends BreakdownElement {

    private String relationshipKind;



    public spem_WorkProductUseRelationship(
        String relationshipKind    ) {
        super(
        );
        this.relationshipKind = relationshipKind;
    }


    public String getRelationshipkind() {
        return relationshipKind;
    }

    public void setRelationshipkind(String relationshipKind) {
        this.relationshipKind = relationshipKind;
    }


}