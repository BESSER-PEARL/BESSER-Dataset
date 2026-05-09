





import java.util.List;
import java.util.ArrayList;

public class statemachine_Region  {






    private statemachine_Pseudostate statemachine_pseudostate;




    private statemachine_ComplexState statemachine_complexstate;


    public statemachine_Region(
    ) {
    }



    public statemachine_Pseudostate getStatemachine_pseudostate() {
        return statemachine_pseudostate;
    }

    public void setStatemachine_pseudostate(statemachine_Pseudostate statemachine_pseudostate) {
        this.statemachine_pseudostate = statemachine_pseudostate;
    }
    public statemachine_ComplexState getStatemachine_complexstate() {
        return statemachine_complexstate;
    }

    public void setStatemachine_complexstate(statemachine_ComplexState statemachine_complexstate) {
        this.statemachine_complexstate = statemachine_complexstate;
    }

}