





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_NumberValue extends ValueType {

    private float value;



    public SpreadsheetMLSimplified_NumberValue(
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