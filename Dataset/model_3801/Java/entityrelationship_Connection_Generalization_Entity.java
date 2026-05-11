





import java.util.List;
import java.util.ArrayList;

public class entityrelationship_Connection_Generalization_Entity  {

    private String minimum_cardinality;
    private String maximum_cardinality;





    private entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model;




    private entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model;




    private entityrelationship_Entity entityrelationship_entity;


    public entityrelationship_Connection_Generalization_Entity(
        String minimum_cardinality,        String maximum_cardinality    ) {
        this.minimum_cardinality = minimum_cardinality;
        this.maximum_cardinality = maximum_cardinality;
    }


    public String getMinimum_cardinality() {
        return minimum_cardinality;
    }

    public void setMinimum_cardinality(String minimum_cardinality) {
        this.minimum_cardinality = minimum_cardinality;
    }
    public String getMaximum_cardinality() {
        return maximum_cardinality;
    }

    public void setMaximum_cardinality(String maximum_cardinality) {
        this.maximum_cardinality = maximum_cardinality;
    }

    public entityrelationship_Entity_Relationship_Model getEntityrelationship_entity_relationship_model() {
        return entityrelationship_entity_relationship_model;
    }

    public void setEntityrelationship_entity_relationship_model(entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model) {
        this.entityrelationship_entity_relationship_model = entityrelationship_entity_relationship_model;
    }
    public entityrelationship_Entity_Relationship_Model getEntityrelationship_entity_relationship_model() {
        return entityrelationship_entity_relationship_model;
    }

    public void setEntityrelationship_entity_relationship_model(entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model) {
        this.entityrelationship_entity_relationship_model = entityrelationship_entity_relationship_model;
    }
    public entityrelationship_Entity getEntityrelationship_entity() {
        return entityrelationship_entity;
    }

    public void setEntityrelationship_entity(entityrelationship_Entity entityrelationship_entity) {
        this.entityrelationship_entity = entityrelationship_entity;
    }

}