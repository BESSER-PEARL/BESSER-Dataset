





import java.util.List;
import java.util.ArrayList;

public class helloWorldDsl_Greeting  {

    private String name;





    private helloWorldDsl_Model helloworlddsl_model;


    public helloWorldDsl_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public helloWorldDsl_Model getHelloworlddsl_model() {
        return helloworlddsl_model;
    }

    public void setHelloworlddsl_model(helloWorldDsl_Model helloworlddsl_model) {
        this.helloworlddsl_model = helloworlddsl_model;
    }

}