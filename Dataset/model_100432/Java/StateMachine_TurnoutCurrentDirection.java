





import java.util.List;
import java.util.ArrayList;

public class StateMachine_TurnoutCurrentDirection extends GuardExpression {

    private String currentTurnoutDirection;





    private StateMachine_Turnout statemachine_turnout;


    public StateMachine_TurnoutCurrentDirection(
        String currentTurnoutDirection    ) {
        super(
        );
        this.currentTurnoutDirection = currentTurnoutDirection;
    }


    public String getCurrentturnoutdirection() {
        return currentTurnoutDirection;
    }

    public void setCurrentturnoutdirection(String currentTurnoutDirection) {
        this.currentTurnoutDirection = currentTurnoutDirection;
    }

    public StateMachine_Turnout getStatemachine_turnout() {
        return statemachine_turnout;
    }

    public void setStatemachine_turnout(StateMachine_Turnout statemachine_turnout) {
        this.statemachine_turnout = statemachine_turnout;
    }

}