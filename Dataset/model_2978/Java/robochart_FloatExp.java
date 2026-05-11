





import java.util.List;
import java.util.ArrayList;

public class robochart_FloatExp extends Expression {

    private float value;



    public robochart_FloatExp(
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