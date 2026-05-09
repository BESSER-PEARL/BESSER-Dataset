





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_SetState extends PosConditionExpression {






    private State state;


    public HALL_FSMInstructions_SetState(
    ) {
        super(
        );
    }



    public State getState() {
        return state;
    }

    public void setState(State state) {
        this.state = state;
    }

}