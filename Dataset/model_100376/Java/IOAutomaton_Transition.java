





import java.util.List;
import java.util.ArrayList;

public class IOAutomaton_Transition  {

    private String name;





    private IOAutomaton_State ioautomaton_state;




    private IOAutomaton_Input ioautomaton_input;




    private IOAutomaton_State ioautomaton_state;




    private IOAutomaton_Activation ioautomaton_activation;




    private IOAutomaton_Automaton ioautomaton_automaton;


    public IOAutomaton_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public IOAutomaton_State getIoautomaton_state() {
        return ioautomaton_state;
    }

    public void setIoautomaton_state(IOAutomaton_State ioautomaton_state) {
        this.ioautomaton_state = ioautomaton_state;
    }
    public IOAutomaton_Input getIoautomaton_input() {
        return ioautomaton_input;
    }

    public void setIoautomaton_input(IOAutomaton_Input ioautomaton_input) {
        this.ioautomaton_input = ioautomaton_input;
    }
    public IOAutomaton_State getIoautomaton_state() {
        return ioautomaton_state;
    }

    public void setIoautomaton_state(IOAutomaton_State ioautomaton_state) {
        this.ioautomaton_state = ioautomaton_state;
    }
    public IOAutomaton_Activation getIoautomaton_activation() {
        return ioautomaton_activation;
    }

    public void setIoautomaton_activation(IOAutomaton_Activation ioautomaton_activation) {
        this.ioautomaton_activation = ioautomaton_activation;
    }
    public IOAutomaton_Automaton getIoautomaton_automaton() {
        return ioautomaton_automaton;
    }

    public void setIoautomaton_automaton(IOAutomaton_Automaton ioautomaton_automaton) {
        this.ioautomaton_automaton = ioautomaton_automaton;
    }

}