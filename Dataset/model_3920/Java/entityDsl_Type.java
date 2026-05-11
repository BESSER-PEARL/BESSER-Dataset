





import java.util.List;
import java.util.ArrayList;

public class entityDsl_Type  {

    private String name;





    private entityDsl_Model entitydsl_model;


    public entityDsl_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entityDsl_Model getEntitydsl_model() {
        return entitydsl_model;
    }

    public void setEntitydsl_model(entityDsl_Model entitydsl_model) {
        this.entitydsl_model = entitydsl_model;
    }

}