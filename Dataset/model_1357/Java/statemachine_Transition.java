





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition extends Named {

    private boolean preserveTimers;





    private statemachine_GAbstractState statemachine_gabstractstate;




    private statemachine_GAbstractState statemachine_gabstractstate;


    public statemachine_Transition(
        boolean preserveTimers    ) {
        super(
        );
        this.preserveTimers = preserveTimers;
    }


    public boolean getPreservetimers() {
        return preserveTimers;
    }

    public void setPreservetimers(boolean preserveTimers) {
        this.preserveTimers = preserveTimers;
    }

    public statemachine_GAbstractState getStatemachine_gabstractstate() {
        return statemachine_gabstractstate;
    }

    public void setStatemachine_gabstractstate(statemachine_GAbstractState statemachine_gabstractstate) {
        this.statemachine_gabstractstate = statemachine_gabstractstate;
    }
    public statemachine_GAbstractState getStatemachine_gabstractstate() {
        return statemachine_gabstractstate;
    }

    public void setStatemachine_gabstractstate(statemachine_GAbstractState statemachine_gabstractstate) {
        this.statemachine_gabstractstate = statemachine_gabstractstate;
    }

}