





import java.util.List;
import java.util.ArrayList;

public class becontent_Reference extends EntityField {

    private String name;





    private becontent_Entity becontent_entity;


    public becontent_Reference(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public becontent_Entity getBecontent_entity() {
        return becontent_entity;
    }

    public void setBecontent_entity(becontent_Entity becontent_entity) {
        this.becontent_entity = becontent_entity;
    }

}