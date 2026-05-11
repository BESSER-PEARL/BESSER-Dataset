





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_Schema  {

    private String name;





    private esper2Maude_Model esper2maude_model;


    public esper2Maude_Schema(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esper2Maude_Model getEsper2maude_model() {
        return esper2maude_model;
    }

    public void setEsper2maude_model(esper2Maude_Model esper2maude_model) {
        this.esper2maude_model = esper2maude_model;
    }

}