





import java.util.List;
import java.util.ArrayList;

public class model_ContinuosAction extends Action {

    private float duration;



    public model_ContinuosAction(
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