





import java.util.List;
import java.util.ArrayList;

public class MDAIntermediateStateMachine_Value  {

    private String value;





    private MDAIntermediateStateMachine_Transition mdaintermediatestatemachine_transition;




    private MDAIntermediateStateMachine_Message mdaintermediatestatemachine_message;


    public MDAIntermediateStateMachine_Value(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public MDAIntermediateStateMachine_Transition getMdaintermediatestatemachine_transition() {
        return mdaintermediatestatemachine_transition;
    }

    public void setMdaintermediatestatemachine_transition(MDAIntermediateStateMachine_Transition mdaintermediatestatemachine_transition) {
        this.mdaintermediatestatemachine_transition = mdaintermediatestatemachine_transition;
    }
    public MDAIntermediateStateMachine_Message getMdaintermediatestatemachine_message() {
        return mdaintermediatestatemachine_message;
    }

    public void setMdaintermediatestatemachine_message(MDAIntermediateStateMachine_Message mdaintermediatestatemachine_message) {
        this.mdaintermediatestatemachine_message = mdaintermediatestatemachine_message;
    }

}