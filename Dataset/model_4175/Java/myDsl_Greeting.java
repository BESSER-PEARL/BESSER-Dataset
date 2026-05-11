





import java.util.List;
import java.util.ArrayList;

public class myDsl_Greeting  {

    private String name;





    private myDsl_Model mydsl_model;


    public myDsl_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}