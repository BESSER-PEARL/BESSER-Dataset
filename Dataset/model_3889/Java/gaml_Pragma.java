





import java.util.List;
import java.util.ArrayList;

public class gaml_Pragma  {

    private String name;





    private gaml_Model gaml_model;


    public gaml_Pragma(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gaml_Model getGaml_model() {
        return gaml_model;
    }

    public void setGaml_model(gaml_Model gaml_model) {
        this.gaml_model = gaml_model;
    }

}