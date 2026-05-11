





import java.util.List;
import java.util.ArrayList;

public class myDot_Entity  {

    private String name;





    private myDot_Model mydot_model;


    public myDot_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDot_Model getMydot_model() {
        return mydot_model;
    }

    public void setMydot_model(myDot_Model mydot_model) {
        this.mydot_model = mydot_model;
    }

}