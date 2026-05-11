





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_CloudMLModel extends CloudMLElementWithProperties {






    private List<ExecuteInstance> executeinstances;




    private List<RelationshipInstance> relationshipinstances;




    private List<Relationship> relationships;


    public cloudml_core_CloudMLModel(
    ) {
        super(
        );
        this.executeinstances = new ArrayList<>();
        this.relationshipinstances = new ArrayList<>();
        this.relationships = new ArrayList<>();
    }

    public cloudml_core_CloudMLModel(
        ArrayList<ExecuteInstance> executeinstances,        ArrayList<RelationshipInstance> relationshipinstances,        ArrayList<Relationship> relationships    ) {
        this.executeinstances = executeinstances;
        this.relationshipinstances = relationshipinstances;
        this.relationships = relationships;
    }


    public List<ExecuteInstance> getExecuteinstances() {
        return executeinstances;
    }

    public void addExecuteinstance(Executeinstance executeinstance) {
        this.executeinstances.add(executeinstance);
    }
    public List<RelationshipInstance> getRelationshipinstances() {
        return relationshipinstances;
    }

    public void addRelationshipinstance(Relationshipinstance relationshipinstance) {
        this.relationshipinstances.add(relationshipinstance);
    }
    public List<Relationship> getRelationships() {
        return relationships;
    }

    public void addRelationship(Relationship relationship) {
        this.relationships.add(relationship);
    }

}