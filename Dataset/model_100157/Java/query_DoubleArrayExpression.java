





import java.util.List;
import java.util.ArrayList;

public class query_DoubleArrayExpression extends ArrayExpression {

    private float values;



    public query_DoubleArrayExpression(
        float values    ) {
        super(
        );
        this.values = values;
    }


    public float getValues() {
        return values;
    }

    public void setValues(float values) {
        this.values = values;
    }


}