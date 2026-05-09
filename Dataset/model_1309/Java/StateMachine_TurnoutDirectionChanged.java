





import java.util.List;
import java.util.ArrayList;

public class StateMachine_TurnoutDirectionChanged extends TriggerExpression {

    private String newTurnoutDirection;





    private StateMachine_Turnout statemachine_turnout;


    public StateMachine_TurnoutDirectionChanged(
        String newTurnoutDirection    ) {
        super(
        );
        this.newTurnoutDirection = newTurnoutDirection;
    }


    public String getNewturnoutdirection() {
        return newTurnoutDirection;
    }

    public void setNewturnoutdirection(String newTurnoutDirection) {
        this.newTurnoutDirection = newTurnoutDirection;
    }

    public StateMachine_Turnout getStatemachine_turnout() {
        return statemachine_turnout;
    }

    public void setStatemachine_turnout(StateMachine_Turnout statemachine_turnout) {
        this.statemachine_turnout = statemachine_turnout;
    }

}