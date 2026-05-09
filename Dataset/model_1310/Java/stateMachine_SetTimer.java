





import java.util.List;
import java.util.ArrayList;

public class stateMachine_SetTimer extends Action {

    private float millis;



    public stateMachine_SetTimer(
        float millis    ) {
        super(
        );
        this.millis = millis;
    }


    public float getMillis() {
        return millis;
    }

    public void setMillis(float millis) {
        this.millis = millis;
    }


}