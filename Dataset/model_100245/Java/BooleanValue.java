





import java.util.List;
import java.util.ArrayList;

public class BooleanValue extends ValueType {

    private boolean value;



    public BooleanValue(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}