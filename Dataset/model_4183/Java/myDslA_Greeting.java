





import java.util.List;
import java.util.ArrayList;

public class myDslA_Greeting  {

    private String name;





    private myDslA_Model mydsla_model;


    public myDslA_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDslA_Model getMydsla_model() {
        return mydsla_model;
    }

    public void setMydsla_model(myDslA_Model mydsla_model) {
        this.mydsla_model = mydsla_model;
    }

}