





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition extends Node {

    private float seconds;



    public petrinet_Transition(
        float seconds    ) {
        super(
        );
        this.seconds = seconds;
    }


    public float getSeconds() {
        return seconds;
    }

    public void setSeconds(float seconds) {
        this.seconds = seconds;
    }


}