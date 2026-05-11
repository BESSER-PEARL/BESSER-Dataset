





import java.util.List;
import java.util.ArrayList;

public class ioautomaton_Operation  {

    private String name;





    private ioautomaton_Transition ioautomaton_transition;


    public ioautomaton_Operation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioautomaton_Transition getIoautomaton_transition() {
        return ioautomaton_transition;
    }

    public void setIoautomaton_transition(ioautomaton_Transition ioautomaton_transition) {
        this.ioautomaton_transition = ioautomaton_transition;
    }

}