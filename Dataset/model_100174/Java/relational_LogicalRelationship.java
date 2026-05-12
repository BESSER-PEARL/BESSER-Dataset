





import java.util.List;
import java.util.ArrayList;

public class relational_LogicalRelationship extends Relationship {






    private relational_Catalog relational_catalog;




    private relational_Catalog relational_catalog;




    private relational_Schema relational_schema;




    private relational_Schema relational_schema;




    private List<relational_LogicalRelationshipEnd> relational_logicalrelationshipends;




    private relational_LogicalRelationshipEnd relational_logicalrelationshipend;


    public relational_LogicalRelationship(
    ) {
        super(
        );
        this.relational_logicalrelationshipends = new ArrayList<>();
    }

    public relational_LogicalRelationship(
        ArrayList<relational_LogicalRelationshipEnd> relational_logicalrelationshipends    ) {
        this.relational_logicalrelationshipends = relational_logicalrelationshipends;
    }


    public relational_Catalog getRelational_catalog() {
        return relational_catalog;
    }

    public void setRelational_catalog(relational_Catalog relational_catalog) {
        this.relational_catalog = relational_catalog;
    }
    public relational_Catalog getRelational_catalog() {
        return relational_catalog;
    }

    public void setRelational_catalog(relational_Catalog relational_catalog) {
        this.relational_catalog = relational_catalog;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public relational_Schema getRelational_schema() {
        return relational_schema;
    }

    public void setRelational_schema(relational_Schema relational_schema) {
        this.relational_schema = relational_schema;
    }
    public List<relational_LogicalRelationshipEnd> getRelational_logicalrelationshipends() {
        return relational_logicalrelationshipends;
    }

    public void addRelational_logicalrelationshipend(Relational_logicalrelationshipend relational_logicalrelationshipend) {
        this.relational_logicalrelationshipends.add(relational_logicalrelationshipend);
    }
    public relational_LogicalRelationshipEnd getRelational_logicalrelationshipend() {
        return relational_logicalrelationshipend;
    }

    public void setRelational_logicalrelationshipend(relational_LogicalRelationshipEnd relational_logicalrelationshipend) {
        this.relational_logicalrelationshipend = relational_logicalrelationshipend;
    }

}