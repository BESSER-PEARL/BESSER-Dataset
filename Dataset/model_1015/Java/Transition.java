





import java.util.List;
import java.util.ArrayList;

public class Transition  {






    private HALL_FSM_State hall_fsm_state;




    private HALL_FSMActions_ActionExpression hall_fsmactions_actionexpression;




    private HALL_FSMConditions_PreConditionExpression hall_fsmconditions_preconditionexpression;




    private HALL_FSMInstructions_PosConditionExpression hall_fsminstructions_posconditionexpression;


    public Transition(
    ) {
    }



    public HALL_FSM_State getHall_fsm_state() {
        return hall_fsm_state;
    }

    public void setHall_fsm_state(HALL_FSM_State hall_fsm_state) {
        this.hall_fsm_state = hall_fsm_state;
    }
    public HALL_FSMActions_ActionExpression getHall_fsmactions_actionexpression() {
        return hall_fsmactions_actionexpression;
    }

    public void setHall_fsmactions_actionexpression(HALL_FSMActions_ActionExpression hall_fsmactions_actionexpression) {
        this.hall_fsmactions_actionexpression = hall_fsmactions_actionexpression;
    }
    public HALL_FSMConditions_PreConditionExpression getHall_fsmconditions_preconditionexpression() {
        return hall_fsmconditions_preconditionexpression;
    }

    public void setHall_fsmconditions_preconditionexpression(HALL_FSMConditions_PreConditionExpression hall_fsmconditions_preconditionexpression) {
        this.hall_fsmconditions_preconditionexpression = hall_fsmconditions_preconditionexpression;
    }
    public HALL_FSMInstructions_PosConditionExpression getHall_fsminstructions_posconditionexpression() {
        return hall_fsminstructions_posconditionexpression;
    }

    public void setHall_fsminstructions_posconditionexpression(HALL_FSMInstructions_PosConditionExpression hall_fsminstructions_posconditionexpression) {
        this.hall_fsminstructions_posconditionexpression = hall_fsminstructions_posconditionexpression;
    }

}