





import java.util.List;
import java.util.ArrayList;

public class ir_RealConstant extends Expression {

    private float value;



    public ir_RealConstant(
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