





import java.util.List;
import java.util.ArrayList;

public class entityDsl_Attribute  {

    private String required;
    private String name;





    private entityDsl_Entity entitydsl_entity;


    public entityDsl_Attribute(
        String required,        String name    ) {
        this.required = required;
        this.name = name;
    }


    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entityDsl_Entity getEntitydsl_entity() {
        return entitydsl_entity;
    }

    public void setEntitydsl_entity(entityDsl_Entity entitydsl_entity) {
        this.entitydsl_entity = entitydsl_entity;
    }

}