





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition extends Named {

    private boolean preserveTimers;





    private statemachine_GAbstractState statemachine_gabstractstate;




    private statemachine_GCompositeState statemachine_gcompositestate;




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
    public statemachine_GCompositeState getStatemachine_gcompositestate() {
        return statemachine_gcompositestate;
    }

    public void setStatemachine_gcompositestate(statemachine_GCompositeState statemachine_gcompositestate) {
        this.statemachine_gcompositestate = statemachine_gcompositestate;
    }
    public statemachine_GAbstractState getStatemachine_gabstractstate() {
        return statemachine_gabstractstate;
    }

    public void setStatemachine_gabstractstate(statemachine_GAbstractState statemachine_gabstractstate) {
        this.statemachine_gabstractstate = statemachine_gabstractstate;
    }

}