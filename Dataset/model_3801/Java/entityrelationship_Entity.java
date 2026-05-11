





import java.util.List;
import java.util.ArrayList;

public class entityrelationship_Entity extends Elements_with_Attributes {

    private String type_entity;
    private String name_entity;



    public entityrelationship_Entity(
        String type_entity,        String name_entity    ) {
        super(
        );
        this.type_entity = type_entity;
        this.name_entity = name_entity;
    }


    public String getType_entity() {
        return type_entity;
    }

    public void setType_entity(String type_entity) {
        this.type_entity = type_entity;
    }
    public String getName_entity() {
        return name_entity;
    }

    public void setName_entity(String name_entity) {
        this.name_entity = name_entity;
    }


}