





import java.util.List;
import java.util.ArrayList;

public class entities_Attribute  {

    private String name;





    private entities_Entity entities_entity;




    private entities_AttributeType entities_attributetype;


    public entities_Attribute(
        String name    ) {
        this.name = name;
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
    public entities_AttributeType getEntities_attributetype() {
        return entities_attributetype;
    }

    public void setEntities_attributetype(entities_AttributeType entities_attributetype) {
        this.entities_attributetype = entities_attributetype;
    }

}