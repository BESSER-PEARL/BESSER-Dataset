





import java.util.List;
import java.util.ArrayList;

public class entityDsl_Property  {

    private String name;
    private boolean many;





    private entityDsl_Entity entitydsl_entity;




    private entityDsl_Type entitydsl_type;


    public entityDsl_Property(
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

    public entityDsl_Entity getEntitydsl_entity() {
        return entitydsl_entity;
    }

    public void setEntitydsl_entity(entityDsl_Entity entitydsl_entity) {
        this.entitydsl_entity = entitydsl_entity;
    }
    public entityDsl_Type getEntitydsl_type() {
        return entitydsl_type;
    }

    public void setEntitydsl_type(entityDsl_Type entitydsl_type) {
        this.entitydsl_type = entitydsl_type;
    }

}