





import java.util.List;
import java.util.ArrayList;

public class base_RealLiteral extends NumberLiteral {

    private float value;



    public base_RealLiteral(
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