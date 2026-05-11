





import java.util.List;
import java.util.ArrayList;

public class robot_Movement extends Operation {

    private float duration;



    public robot_Movement(
        float duration    ) {
        super(
        );
        this.duration = duration;
    }


    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
    }


}