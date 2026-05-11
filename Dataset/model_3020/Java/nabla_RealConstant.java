





import java.util.List;
import java.util.ArrayList;

public class nabla_RealConstant extends Expression {

    private float value;



    public nabla_RealConstant(
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