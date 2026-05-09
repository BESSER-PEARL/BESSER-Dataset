





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private boolean initial;
    private boolean terminal;



    public statemachine_State(
        boolean initial,        boolean terminal    ) {
        this.initial = initial;
        this.terminal = terminal;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public boolean getTerminal() {
        return terminal;
    }

    public void setTerminal(boolean terminal) {
        this.terminal = terminal;
    }


}