





import java.util.List;
import java.util.ArrayList;

public class ioautomaton_Return  {

    private String value;





    private ioautomaton_Transition ioautomaton_transition;


    public ioautomaton_Return(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public ioautomaton_Transition getIoautomaton_transition() {
        return ioautomaton_transition;
    }

    public void setIoautomaton_transition(ioautomaton_Transition ioautomaton_transition) {
        this.ioautomaton_transition = ioautomaton_transition;
    }

}