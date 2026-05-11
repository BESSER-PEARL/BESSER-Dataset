





import java.util.List;
import java.util.ArrayList;

public class activator_Greeting  {

    private String name;





    private activator_Model activator_model;


    public activator_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public activator_Model getActivator_model() {
        return activator_model;
    }

    public void setActivator_model(activator_Model activator_model) {
        this.activator_model = activator_model;
    }

}