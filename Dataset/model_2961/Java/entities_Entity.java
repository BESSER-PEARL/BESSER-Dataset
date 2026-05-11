





import java.util.List;
import java.util.ArrayList;

public class entities_Entity  {

    private String name;





    private entities_Model entities_model;




    private entities_EntityType entities_entitytype;




    private entities_Entity entities_entity;


    public entities_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public entities_Entity getEntities_entity() {
        return entities_entity;
    }

    public void setEntities_entity(entities_Entity entities_entity) {
        this.entities_entity = entities_entity;
    }

}