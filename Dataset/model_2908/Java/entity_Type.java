





import java.util.List;
import java.util.ArrayList;

public class entity_Type  {

    private String name;





    private entity_Model entity_model;


    public entity_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entity_Model getEntity_model() {
        return entity_model;
    }

    public void setEntity_model(entity_Model entity_model) {
        this.entity_model = entity_model;
    }

}