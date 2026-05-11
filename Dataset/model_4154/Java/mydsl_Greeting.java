





import java.util.List;
import java.util.ArrayList;

public class mydsl_Greeting  {

    private String name;





    private mydsl_Model mydsl_model;


    public mydsl_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mydsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(mydsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}