





import java.util.List;
import java.util.ArrayList;

public class entity_Attribute extends NamedElement {






    private entity_Datatype entity_datatype;




    private entity_Entity entity_entity;


    public entity_Attribute(
    ) {
        super(
        );
    }



    public entity_Datatype getEntity_datatype() {
        return entity_datatype;
    }

    public void setEntity_datatype(entity_Datatype entity_datatype) {
        this.entity_datatype = entity_datatype;
    }
    public entity_Entity getEntity_entity() {
        return entity_entity;
    }

    public void setEntity_entity(entity_Entity entity_entity) {
        this.entity_entity = entity_entity;
    }

}