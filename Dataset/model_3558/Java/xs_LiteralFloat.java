





import java.util.List;
import java.util.ArrayList;

public class xs_LiteralFloat extends Literal {

    private float value;



    public xs_LiteralFloat(
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