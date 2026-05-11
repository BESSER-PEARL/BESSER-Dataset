





import java.util.List;
import java.util.ArrayList;

public class House2_GreaterThanCondition extends Condition {

    private float threshold;



    public House2_GreaterThanCondition(
        float threshold    ) {
        super(
        );
        this.threshold = threshold;
    }


    public float getThreshold() {
        return threshold;
    }

    public void setThreshold(float threshold) {
        this.threshold = threshold;
    }


}