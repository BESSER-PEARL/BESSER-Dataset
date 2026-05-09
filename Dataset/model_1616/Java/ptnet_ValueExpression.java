





import java.util.List;
import java.util.ArrayList;

public class ptnet_ValueExpression extends ArithmeticExpression {

    private float value;



    public ptnet_ValueExpression(
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