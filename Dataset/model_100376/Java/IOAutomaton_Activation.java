





import java.util.List;
import java.util.ArrayList;

public class IOAutomaton_Activation  {

    private String name;





    private IOAutomaton_Automaton ioautomaton_automaton;


    public IOAutomaton_Activation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public IOAutomaton_Automaton getIoautomaton_automaton() {
        return ioautomaton_automaton;
    }

    public void setIoautomaton_automaton(IOAutomaton_Automaton ioautomaton_automaton) {
        this.ioautomaton_automaton = ioautomaton_automaton;
    }

}