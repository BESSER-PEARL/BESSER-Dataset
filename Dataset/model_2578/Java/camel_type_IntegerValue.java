





import java.util.List;
import java.util.ArrayList;

public class camel_type_IntegerValue extends NumericValue {

    private int value;



    public camel_type_IntegerValue(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}