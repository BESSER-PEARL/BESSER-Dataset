





import java.util.List;
import java.util.ArrayList;

public class problog_ProbabilityLiteral extends ProbabilityMeasure {

    private float value;



    public problog_ProbabilityLiteral(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}