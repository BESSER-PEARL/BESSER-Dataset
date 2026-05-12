





import java.util.List;
import java.util.ArrayList;

public class automaton_TimedZone  {

    private String time;





    private automaton_Automaton automaton_automaton;


    public automaton_TimedZone(
        String time    ) {
        this.time = time;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }

}