





import java.util.List;
import java.util.ArrayList;

public class autopl_State  {

    private String isInitial;
    private String name;
    private String isFinal;





    private autopl_Automaton autopl_automaton;


    public autopl_State(
        String isInitial,        String name,        String isFinal    ) {
        this.isInitial = isInitial;
        this.name = name;
        this.isFinal = isFinal;
    }


    public String getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(String isInitial) {
        this.isInitial = isInitial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(String isFinal) {
        this.isFinal = isFinal;
    }

    public autopl_Automaton getAutopl_automaton() {
        return autopl_automaton;
    }

    public void setAutopl_automaton(autopl_Automaton autopl_automaton) {
        this.autopl_automaton = autopl_automaton;
    }

}