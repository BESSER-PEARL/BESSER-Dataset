





import java.util.List;
import java.util.ArrayList;

public class entities_Type  {

    private String name;





    private entities_Model entities_model;




    private entities_Property entities_property;


    public entities_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entities_Model getEntities_model() {
        return entities_model;
    }

    public void setEntities_model(entities_Model entities_model) {
        this.entities_model = entities_model;
    }
    public entities_Property getEntities_property() {
        return entities_property;
    }

    public void setEntities_property(entities_Property entities_property) {
        this.entities_property = entities_property;
    }

}