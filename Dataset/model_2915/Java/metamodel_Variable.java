





import java.util.List;
import java.util.ArrayList;

public class metamodel_Variable  {

    private String name;





    private metamodel_Entity metamodel_entity;


    public metamodel_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Entity getMetamodel_entity() {
        return metamodel_entity;
    }

    public void setMetamodel_entity(metamodel_Entity metamodel_entity) {
        this.metamodel_entity = metamodel_entity;
    }

}