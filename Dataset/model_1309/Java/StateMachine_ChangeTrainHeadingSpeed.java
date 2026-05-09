





import java.util.List;
import java.util.ArrayList;

public class StateMachine_ChangeTrainHeadingSpeed extends ActionExpression {

    private String newHeadingSpeed;





    private StateMachine_Train statemachine_train;


    public StateMachine_ChangeTrainHeadingSpeed(
        String newHeadingSpeed    ) {
        super(
        );
        this.newHeadingSpeed = newHeadingSpeed;
    }


    public String getNewheadingspeed() {
        return newHeadingSpeed;
    }

    public void setNewheadingspeed(String newHeadingSpeed) {
        this.newHeadingSpeed = newHeadingSpeed;
    }

    public StateMachine_Train getStatemachine_train() {
        return statemachine_train;
    }

    public void setStatemachine_train(StateMachine_Train statemachine_train) {
        this.statemachine_train = statemachine_train;
    }

}