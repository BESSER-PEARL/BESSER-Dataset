





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_Wait extends SequenceCommand {

    private float duration;



    public farmbot_modeling_Wait(
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