





import java.util.List;
import java.util.ArrayList;

public class urml_Protocol  {

    private String name;





    private urml_Model urml_model;


    public urml_Protocol(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public urml_Model getUrml_model() {
        return urml_model;
    }

    public void setUrml_model(urml_Model urml_model) {
        this.urml_model = urml_model;
    }

}