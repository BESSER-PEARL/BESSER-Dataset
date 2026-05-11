





import java.util.List;
import java.util.ArrayList;

public class resource_Greeting  {

    private String name;





    private resource_Model resource_model;


    public resource_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public resource_Model getResource_model() {
        return resource_model;
    }

    public void setResource_model(resource_Model resource_model) {
        this.resource_model = resource_model;
    }

}