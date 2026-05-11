





import java.util.List;
import java.util.ArrayList;

public class helloWorld_Greeting  {

    private String name;





    private helloWorld_Model helloworld_model;


    public helloWorld_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public helloWorld_Model getHelloworld_model() {
        return helloworld_model;
    }

    public void setHelloworld_model(helloWorld_Model helloworld_model) {
        this.helloworld_model = helloworld_model;
    }

}