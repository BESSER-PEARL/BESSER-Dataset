





import java.util.List;
import java.util.ArrayList;

public class StateMachine_ChangeTurnoutDirection extends ActionExpression {

    private String newTurnoutDirection;



    public StateMachine_ChangeTurnoutDirection(
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


}