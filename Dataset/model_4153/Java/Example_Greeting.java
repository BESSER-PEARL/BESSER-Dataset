





import java.util.List;
import java.util.ArrayList;

public class Example_Greeting  {

    private String name;





    private Example_Model example_model;


    public Example_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Example_Model getExample_model() {
        return example_model;
    }

    public void setExample_model(Example_Model example_model) {
        this.example_model = example_model;
    }

}