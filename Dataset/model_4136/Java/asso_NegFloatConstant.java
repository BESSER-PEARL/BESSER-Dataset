





import java.util.List;
import java.util.ArrayList;

public class asso_NegFloatConstant extends Expression {

    private float value;



    public asso_NegFloatConstant(
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