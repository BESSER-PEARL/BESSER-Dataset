





import java.util.List;
import java.util.ArrayList;

public class statesml_ChangeEvent extends Event {

    private boolean isFulfilled;





    private statesml_Trigger statesml_trigger;


    public statesml_ChangeEvent(
        boolean isFulfilled    ) {
        super(
        );
        this.isFulfilled = isFulfilled;
    }


    public boolean getIsfulfilled() {
        return isFulfilled;
    }

    public void setIsfulfilled(boolean isFulfilled) {
        this.isFulfilled = isFulfilled;
    }

    public statesml_Trigger getStatesml_trigger() {
        return statesml_trigger;
    }

    public void setStatesml_trigger(statesml_Trigger statesml_trigger) {
        this.statesml_trigger = statesml_trigger;
    }

}