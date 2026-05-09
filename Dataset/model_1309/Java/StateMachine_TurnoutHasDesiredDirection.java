





import java.util.List;
import java.util.ArrayList;

public class StateMachine_TurnoutHasDesiredDirection extends GuardExpression {






    private StateMachine_Turnout statemachine_turnout;


    public StateMachine_TurnoutHasDesiredDirection(
    ) {
        super(
        );
    }



    public StateMachine_Turnout getStatemachine_turnout() {
        return statemachine_turnout;
    }

    public void setStatemachine_turnout(StateMachine_Turnout statemachine_turnout) {
        this.statemachine_turnout = statemachine_turnout;
    }

}