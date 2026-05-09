





import java.util.List;
import java.util.ArrayList;

public class spem_WorkProductUseRelationship extends BreakdownElement {

    private String relationshipKind;





    private spem_WorkProductUse spem_workproductuse;




    private List<spem_WorkProductUse> spem_workproductuses;


    public spem_WorkProductUseRelationship(
        String relationshipKind    ) {
        super(
        );
        this.relationshipKind = relationshipKind;
        this.spem_workproductuses = new ArrayList<>();
    }

    public spem_WorkProductUseRelationship(
        String relationshipKind        ArrayList<spem_WorkProductUse> spem_workproductuses    ) {
        this.relationshipKind = relationshipKind;
        this.spem_workproductuses = spem_workproductuses;
    }

    public String getRelationshipkind() {
        return relationshipKind;
    }

    public void setRelationshipkind(String relationshipKind) {
        this.relationshipKind = relationshipKind;
    }

    public spem_WorkProductUse getSpem_workproductuse() {
        return spem_workproductuse;
    }

    public void setSpem_workproductuse(spem_WorkProductUse spem_workproductuse) {
        this.spem_workproductuse = spem_workproductuse;
    }
    public List<spem_WorkProductUse> getSpem_workproductuses() {
        return spem_workproductuses;
    }

    public void addSpem_workproductuse(Spem_workproductuse spem_workproductuse) {
        this.spem_workproductuses.add(spem_workproductuse);
    }

}