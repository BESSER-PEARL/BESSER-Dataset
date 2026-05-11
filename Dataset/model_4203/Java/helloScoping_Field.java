





import java.util.List;
import java.util.ArrayList;

public class helloScoping_Field  {

    private String name;





    private helloScoping_Greeting helloscoping_greeting;


    public helloScoping_Field(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public helloScoping_Greeting getHelloscoping_greeting() {
        return helloscoping_greeting;
    }

    public void setHelloscoping_greeting(helloScoping_Greeting helloscoping_greeting) {
        this.helloscoping_greeting = helloscoping_greeting;
    }

}