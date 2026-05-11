





import java.util.List;
import java.util.ArrayList;

public class myDsl1_Greeting  {

    private String name;





    private myDsl1_Model mydsl1_model;


    public myDsl1_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl1_Model getMydsl1_model() {
        return mydsl1_model;
    }

    public void setMydsl1_model(myDsl1_Model mydsl1_model) {
        this.mydsl1_model = mydsl1_model;
    }

}