





import java.util.List;
import java.util.ArrayList;

public class entities_Property  {

    private String name;
    private boolean many;





    private entities_Type entities_type;




    private entities_Entity entities_entity;


    public entities_Property(
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

    public entities_Type getEntities_type() {
        return entities_type;
    }

    public void setEntities_type(entities_Type entities_type) {
        this.entities_type = entities_type;
    }
    public entities_Entity getEntities_entity() {
        return entities_entity;
    }

    public void setEntities_entity(entities_Entity entities_entity) {
        this.entities_entity = entities_entity;
    }

}