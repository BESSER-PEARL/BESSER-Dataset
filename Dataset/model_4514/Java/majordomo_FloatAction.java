





import java.util.List;
import java.util.ArrayList;

public class majordomo_FloatAction extends Action {

    private float value;





    private majordomo_FloatActor majordomo_floatactor;


    public majordomo_FloatAction(
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

    public majordomo_FloatActor getMajordomo_floatactor() {
        return majordomo_floatactor;
    }

    public void setMajordomo_floatactor(majordomo_FloatActor majordomo_floatactor) {
        this.majordomo_floatactor = majordomo_floatactor;
    }

}