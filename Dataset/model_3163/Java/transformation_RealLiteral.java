





import java.util.List;
import java.util.ArrayList;

public class transformation_RealLiteral extends Expression {

    private float value;



    public transformation_RealLiteral(
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