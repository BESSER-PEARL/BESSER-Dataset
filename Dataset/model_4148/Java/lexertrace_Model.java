





import java.util.List;
import java.util.ArrayList;

public class lexertrace_Model  {






    private List<lexertrace_Greeting> lexertrace_greetings;


    public lexertrace_Model(
    ) {
        this.lexertrace_greetings = new ArrayList<>();
    }

    public lexertrace_Model(
        ArrayList<lexertrace_Greeting> lexertrace_greetings    ) {
        this.lexertrace_greetings = lexertrace_greetings;
    }


    public List<lexertrace_Greeting> getLexertrace_greetings() {
        return lexertrace_greetings;
    }

    public void addLexertrace_greeting(Lexertrace_greeting lexertrace_greeting) {
        this.lexertrace_greetings.add(lexertrace_greeting);
    }

}