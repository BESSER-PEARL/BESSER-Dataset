





import java.util.List;
import java.util.ArrayList;

public class entities_ReferenceProperty extends Property {

    private boolean many;





    private entities_Entity entities_entity;


    public entities_ReferenceProperty(
        boolean many    ) {
        super(
        );
        this.many = many;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public entities_Entity getEntities_entity() {
        return entities_entity;
    }

    public void setEntities_entity(entities_Entity entities_entity) {
        this.entities_entity = entities_entity;
    }

}