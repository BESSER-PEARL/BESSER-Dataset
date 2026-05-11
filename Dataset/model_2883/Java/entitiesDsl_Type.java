





import java.util.List;
import java.util.ArrayList;

public class entitiesDsl_Type  {

    private String name;





    private entitiesDsl_Attribute entitiesdsl_attribute;




    private entitiesDsl_Model entitiesdsl_model;


    public entitiesDsl_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public entitiesDsl_Attribute getEntitiesdsl_attribute() {
        return entitiesdsl_attribute;
    }

    public void setEntitiesdsl_attribute(entitiesDsl_Attribute entitiesdsl_attribute) {
        this.entitiesdsl_attribute = entitiesdsl_attribute;
    }
    public entitiesDsl_Model getEntitiesdsl_model() {
        return entitiesdsl_model;
    }

    public void setEntitiesdsl_model(entitiesDsl_Model entitiesdsl_model) {
        this.entitiesdsl_model = entitiesdsl_model;
    }

}