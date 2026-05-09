





import java.util.List;
import java.util.ArrayList;

public class StateMachine_TrainCurrentHeadingSpeed extends GuardExpression {

    private String currentHeadingSpeed;





    private StateMachine_Train statemachine_train;


    public StateMachine_TrainCurrentHeadingSpeed(
        String currentHeadingSpeed    ) {
        super(
        );
        this.currentHeadingSpeed = currentHeadingSpeed;
    }


    public String getCurrentheadingspeed() {
        return currentHeadingSpeed;
    }

    public void setCurrentheadingspeed(String currentHeadingSpeed) {
        this.currentHeadingSpeed = currentHeadingSpeed;
    }

    public StateMachine_Train getStatemachine_train() {
        return statemachine_train;
    }

    public void setStatemachine_train(StateMachine_Train statemachine_train) {
        this.statemachine_train = statemachine_train;
    }

}