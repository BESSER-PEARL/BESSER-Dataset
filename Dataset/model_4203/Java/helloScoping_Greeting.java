





import java.util.List;
import java.util.ArrayList;

public class helloScoping_Greeting  {

    private String name;





    private helloScoping_Model helloscoping_model;




    private helloScoping_Greeting helloscoping_greeting;


    public helloScoping_Greeting(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public helloScoping_Model getHelloscoping_model() {
        return helloscoping_model;
    }

    public void setHelloscoping_model(helloScoping_Model helloscoping_model) {
        this.helloscoping_model = helloscoping_model;
    }
    public helloScoping_Greeting getHelloscoping_greeting() {
        return helloscoping_greeting;
    }

    public void setHelloscoping_greeting(helloScoping_Greeting helloscoping_greeting) {
        this.helloscoping_greeting = helloscoping_greeting;
    }

}