





import java.util.List;
import java.util.ArrayList;

public class behaviour_Hover extends Move {

    private float duration;



    public behaviour_Hover(
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