





import java.util.List;
import java.util.ArrayList;

public class iot2_BooleanValue extends Value {

    private boolean value;



    public iot2_BooleanValue(
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