





import java.util.List;
import java.util.ArrayList;

public class hello_Greeting  {

    private String name;





    private hello_Model hello_model;


    public hello_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public hello_Model getHello_model() {
        return hello_model;
    }

    public void setHello_model(hello_Model hello_model) {
        this.hello_model = hello_model;
    }

}