





import java.util.List;
import java.util.ArrayList;

public class metamodel_Attribute  {

    private String name;
    private boolean list;





    private metamodel_Entity metamodel_entity;




    private metamodel_Type metamodel_type;


    public metamodel_Attribute(
        String name,        boolean list    ) {
        this.name = name;
        this.list = list;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getList() {
        return list;
    }

    public void setList(boolean list) {
        this.list = list;
    }

    public metamodel_Entity getMetamodel_entity() {
        return metamodel_entity;
    }

    public void setMetamodel_entity(metamodel_Entity metamodel_entity) {
        this.metamodel_entity = metamodel_entity;
    }
    public metamodel_Type getMetamodel_type() {
        return metamodel_type;
    }

    public void setMetamodel_type(metamodel_Type metamodel_type) {
        this.metamodel_type = metamodel_type;
    }

}