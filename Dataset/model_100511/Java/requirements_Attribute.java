





import java.util.List;
import java.util.ArrayList;

public class requirements_Attribute extends BasicElement {

    private String type;





    private requirements_Entity requirements_entity;


    public requirements_Attribute(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public requirements_Entity getRequirements_entity() {
        return requirements_entity;
    }

    public void setRequirements_entity(requirements_Entity requirements_entity) {
        this.requirements_entity = requirements_entity;
    }

}