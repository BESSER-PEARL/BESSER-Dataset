





import java.util.List;
import java.util.ArrayList;

public class sql_literal_ApproximateNumericLiteral extends NumericLiteral {

    private float value;



    public sql_literal_ApproximateNumericLiteral(
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