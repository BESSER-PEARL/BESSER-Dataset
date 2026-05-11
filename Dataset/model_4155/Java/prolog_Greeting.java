





import java.util.List;
import java.util.ArrayList;

public class prolog_Greeting  {

    private String name;





    private prolog_Model prolog_model;


    public prolog_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public prolog_Model getProlog_model() {
        return prolog_model;
    }

    public void setProlog_model(prolog_Model prolog_model) {
        this.prolog_model = prolog_model;
    }

}