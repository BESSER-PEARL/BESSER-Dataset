





import java.util.List;
import java.util.ArrayList;

public class evlDSL_Greeting  {

    private String name;





    private evlDSL_Model evldsl_model;


    public evlDSL_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public evlDSL_Model getEvldsl_model() {
        return evldsl_model;
    }

    public void setEvldsl_model(evlDSL_Model evldsl_model) {
        this.evldsl_model = evldsl_model;
    }

}