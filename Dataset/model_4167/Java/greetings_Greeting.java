





import java.util.List;
import java.util.ArrayList;

public class greetings_Greeting  {

    private String name;





    private greetings_Model greetings_model;


    public greetings_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public greetings_Model getGreetings_model() {
        return greetings_model;
    }

    public void setGreetings_model(greetings_Model greetings_model) {
        this.greetings_model = greetings_model;
    }

}