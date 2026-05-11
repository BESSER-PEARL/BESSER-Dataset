





import java.util.List;
import java.util.ArrayList;

public class entities_Property  {

    private boolean many;
    private String name;





    private entities_Entity entities_entity;


    public entities_Property(
        boolean many,        String name    ) {
        this.many = many;
        this.name = name;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entities_Entity getEntities_entity() {
        return entities_entity;
    }

    public void setEntities_entity(entities_Entity entities_entity) {
        this.entities_entity = entities_entity;
    }

}