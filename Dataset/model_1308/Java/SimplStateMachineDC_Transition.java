





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachineDC_Transition  {

    private String event;





    private SimplStateMachineDC_StateMachine simplstatemachinedc_statemachine;


    public SimplStateMachineDC_Transition(
        String event    ) {
        this.event = event;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public SimplStateMachineDC_StateMachine getSimplstatemachinedc_statemachine() {
        return simplstatemachinedc_statemachine;
    }

    public void setSimplstatemachinedc_statemachine(SimplStateMachineDC_StateMachine simplstatemachinedc_statemachine) {
        this.simplstatemachinedc_statemachine = simplstatemachinedc_statemachine;
    }

}