





import java.util.List;
import java.util.ArrayList;

public class dbca_EntityForm extends Form {

    private String type;





    private dbca_Entity dbca_entity;


    public dbca_EntityForm(
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

    public dbca_Entity getDbca_entity() {
        return dbca_entity;
    }

    public void setDbca_entity(dbca_Entity dbca_entity) {
        this.dbca_entity = dbca_entity;
    }

}