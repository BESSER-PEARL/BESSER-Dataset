





import java.util.List;
import java.util.ArrayList;

public class myDsl2_Greeting  {

    private String name;





    private myDsl2_Model mydsl2_model;


    public myDsl2_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl2_Model getMydsl2_model() {
        return mydsl2_model;
    }

    public void setMydsl2_model(myDsl2_Model mydsl2_model) {
        this.mydsl2_model = mydsl2_model;
    }

}