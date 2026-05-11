





import java.util.List;
import java.util.ArrayList;

public class typesystem_RealLiteral extends NumericLiteral {

    private float value;



    public typesystem_RealLiteral(
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