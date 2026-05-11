





import java.util.List;
import java.util.ArrayList;

public class entityrelationship_Generalization  {

    private String restriction_inheritance_1;
    private String restriction_inheritance_2;





    private entityrelationship_Entity entityrelationship_entity;




    private entityrelationship_Entity entityrelationship_entity;




    private entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model;




    private entityrelationship_Connection_Generalization_Entity entityrelationship_connection_generalization_entity;




    private List<entityrelationship_Entity> entityrelationship_entitys;




    private entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model;


    public entityrelationship_Generalization(
        String restriction_inheritance_1,        String restriction_inheritance_2    ) {
        this.restriction_inheritance_1 = restriction_inheritance_1;
        this.restriction_inheritance_2 = restriction_inheritance_2;
        this.entityrelationship_entitys = new ArrayList<>();
    }

    public entityrelationship_Generalization(
        String restriction_inheritance_1,        String restriction_inheritance_2        ArrayList<entityrelationship_Entity> entityrelationship_entitys    ) {
        this.restriction_inheritance_1 = restriction_inheritance_1;
        this.restriction_inheritance_2 = restriction_inheritance_2;
        this.entityrelationship_entitys = entityrelationship_entitys;
    }

    public String getRestriction_inheritance_1() {
        return restriction_inheritance_1;
    }

    public void setRestriction_inheritance_1(String restriction_inheritance_1) {
        this.restriction_inheritance_1 = restriction_inheritance_1;
    }
    public String getRestriction_inheritance_2() {
        return restriction_inheritance_2;
    }

    public void setRestriction_inheritance_2(String restriction_inheritance_2) {
        this.restriction_inheritance_2 = restriction_inheritance_2;
    }

    public entityrelationship_Entity getEntityrelationship_entity() {
        return entityrelationship_entity;
    }

    public void setEntityrelationship_entity(entityrelationship_Entity entityrelationship_entity) {
        this.entityrelationship_entity = entityrelationship_entity;
    }
    public entityrelationship_Entity getEntityrelationship_entity() {
        return entityrelationship_entity;
    }

    public void setEntityrelationship_entity(entityrelationship_Entity entityrelationship_entity) {
        this.entityrelationship_entity = entityrelationship_entity;
    }
    public entityrelationship_Entity_Relationship_Model getEntityrelationship_entity_relationship_model() {
        return entityrelationship_entity_relationship_model;
    }

    public void setEntityrelationship_entity_relationship_model(entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model) {
        this.entityrelationship_entity_relationship_model = entityrelationship_entity_relationship_model;
    }
    public entityrelationship_Connection_Generalization_Entity getEntityrelationship_connection_generalization_entity() {
        return entityrelationship_connection_generalization_entity;
    }

    public void setEntityrelationship_connection_generalization_entity(entityrelationship_Connection_Generalization_Entity entityrelationship_connection_generalization_entity) {
        this.entityrelationship_connection_generalization_entity = entityrelationship_connection_generalization_entity;
    }
    public List<entityrelationship_Entity> getEntityrelationship_entitys() {
        return entityrelationship_entitys;
    }

    public void addEntityrelationship_entity(Entityrelationship_entity entityrelationship_entity) {
        this.entityrelationship_entitys.add(entityrelationship_entity);
    }
    public entityrelationship_Entity_Relationship_Model getEntityrelationship_entity_relationship_model() {
        return entityrelationship_entity_relationship_model;
    }

    public void setEntityrelationship_entity_relationship_model(entityrelationship_Entity_Relationship_Model entityrelationship_entity_relationship_model) {
        this.entityrelationship_entity_relationship_model = entityrelationship_entity_relationship_model;
    }

}