





import java.util.List;
import java.util.ArrayList;

public class behaviour_Choice extends MoveTransition {

    private String conditionIdentifier;





    private behaviour_Move behaviour_move;


    public behaviour_Choice(
        String conditionIdentifier    ) {
        super(
        );
        this.conditionIdentifier = conditionIdentifier;
    }


    public String getConditionidentifier() {
        return conditionIdentifier;
    }

    public void setConditionidentifier(String conditionIdentifier) {
        this.conditionIdentifier = conditionIdentifier;
    }

    public behaviour_Move getBehaviour_move() {
        return behaviour_move;
    }

    public void setBehaviour_move(behaviour_Move behaviour_move) {
        this.behaviour_move = behaviour_move;
    }

}