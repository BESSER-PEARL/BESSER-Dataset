





import java.util.List;
import java.util.ArrayList;

public class tfsm_TimedTransition extends Transition {






    private tfsm_ClockConstraintOperation tfsm_clockconstraintoperation;


    public tfsm_TimedTransition(
    ) {
        super(
        );
    }



    public tfsm_ClockConstraintOperation getTfsm_clockconstraintoperation() {
        return tfsm_clockconstraintoperation;
    }

    public void setTfsm_clockconstraintoperation(tfsm_ClockConstraintOperation tfsm_clockconstraintoperation) {
        this.tfsm_clockconstraintoperation = tfsm_clockconstraintoperation;
    }

}