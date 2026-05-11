





import java.util.List;
import java.util.ArrayList;

public class asso_FloatConstant extends Expression {

    private float value;



    public asso_FloatConstant(
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