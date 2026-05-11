





import java.util.List;
import java.util.ArrayList;

public class entity_Attribute  {

    private String name;
    private boolean many;





    private entity_Type entity_type;




    private entity_Entity entity_entity;


    public entity_Attribute(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public entity_Type getEntity_type() {
        return entity_type;
    }

    public void setEntity_type(entity_Type entity_type) {
        this.entity_type = entity_type;
    }
    public entity_Entity getEntity_entity() {
        return entity_entity;
    }

    public void setEntity_entity(entity_Entity entity_entity) {
        this.entity_entity = entity_entity;
    }

}