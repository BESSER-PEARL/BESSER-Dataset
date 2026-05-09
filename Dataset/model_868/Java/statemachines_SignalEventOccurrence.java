





import java.util.List;
import java.util.ArrayList;

public class statemachines_SignalEventOccurrence extends EventOccurrence {






    private statemachines_Behavior statemachines_behavior;




    private statemachines_Signal statemachines_signal;


    public statemachines_SignalEventOccurrence(
    ) {
        super(
        );
    }



    public statemachines_Behavior getStatemachines_behavior() {
        return statemachines_behavior;
    }

    public void setStatemachines_behavior(statemachines_Behavior statemachines_behavior) {
        this.statemachines_behavior = statemachines_behavior;
    }
    public statemachines_Signal getStatemachines_signal() {
        return statemachines_signal;
    }

    public void setStatemachines_signal(statemachines_Signal statemachines_signal) {
        this.statemachines_signal = statemachines_signal;
    }

}