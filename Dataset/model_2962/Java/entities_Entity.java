





import java.util.List;
import java.util.ArrayList;

public class entities_Entity  {

    private String name_id;





    private List<entities_Attribute> entities_attributes;




    private entities_Entity entities_entity;




    private entities_Model entities_model;




    private entities_EntityType entities_entitytype;


    public entities_Entity(
        String name_id    ) {
        this.name_id = name_id;
        this.entities_attributes = new ArrayList<>();
    }

    public entities_Entity(
        String name_id        ArrayList<entities_Attribute> entities_attributes    ) {
        this.name_id = name_id;
        this.entities_attributes = entities_attributes;
    }

    public String getName_id() {
        return name_id;
    }

    public void setName_id(String name_id) {
        this.name_id = name_id;
    }

    public List<entities_Attribute> getEntities_attributes() {
        return entities_attributes;
    }

    public void addEntities_attribute(Entities_attribute entities_attribute) {
        this.entities_attributes.add(entities_attribute);
    }
    public entities_Entity getEntities_entity() {
        return entities_entity;
    }

    public void setEntities_entity(entities_Entity entities_entity) {
        this.entities_entity = entities_entity;
    }
    public entities_Model getEntities_model() {
        return entities_model;
    }

    public void setEntities_model(entities_Model entities_model) {
        this.entities_model = entities_model;
    }
    public entities_EntityType getEntities_entitytype() {
        return entities_entitytype;
    }

    public void setEntities_entitytype(entities_EntityType entities_entitytype) {
        this.entities_entitytype = entities_entitytype;
    }

}