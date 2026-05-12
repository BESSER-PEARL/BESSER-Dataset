





import java.util.List;
import java.util.ArrayList;

public class StateMachine_ChangeTrainHeadingSpeed extends ActionExpression {

    private String newHeadingSpeed;



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


}