





import java.util.List;
import java.util.ArrayList;

public class go_FunctionBody  {






    private List<go_Greeting> go_greetings;




    private go_DecFunc go_decfunc;


    public go_FunctionBody(
    ) {
        this.go_greetings = new ArrayList<>();
    }

    public go_FunctionBody(
        ArrayList<go_Greeting> go_greetings    ) {
        this.go_greetings = go_greetings;
    }


    public List<go_Greeting> getGo_greetings() {
        return go_greetings;
    }

    public void addGo_greeting(Go_greeting go_greeting) {
        this.go_greetings.add(go_greeting);
    }
    public go_DecFunc getGo_decfunc() {
        return go_decfunc;
    }

    public void setGo_decfunc(go_DecFunc go_decfunc) {
        this.go_decfunc = go_decfunc;
    }

}