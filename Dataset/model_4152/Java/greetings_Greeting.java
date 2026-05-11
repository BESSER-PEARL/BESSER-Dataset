





import java.util.List;
import java.util.ArrayList;

public class greetings_Greeting  {

    private String name;





    private greetings_GreetingsModel greetings_greetingsmodel;


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

    public greetings_GreetingsModel getGreetings_greetingsmodel() {
        return greetings_greetingsmodel;
    }

    public void setGreetings_greetingsmodel(greetings_GreetingsModel greetings_greetingsmodel) {
        this.greetings_greetingsmodel = greetings_greetingsmodel;
    }

}