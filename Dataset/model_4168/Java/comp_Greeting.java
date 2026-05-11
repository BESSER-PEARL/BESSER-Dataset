





import java.util.List;
import java.util.ArrayList;

public class comp_Greeting  {

    private String name;





    private comp_Model comp_model;


    public comp_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public comp_Model getComp_model() {
        return comp_model;
    }

    public void setComp_model(comp_Model comp_model) {
        this.comp_model = comp_model;
    }

}