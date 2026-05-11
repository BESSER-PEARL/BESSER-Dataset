





import java.util.List;
import java.util.ArrayList;

public class expressions_FloatingPointLiteral extends Expression {

    private float value;



    public expressions_FloatingPointLiteral(
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