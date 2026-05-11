





import java.util.List;
import java.util.ArrayList;

public class imp_BoolValue extends Value {

    private boolean value;



    public imp_BoolValue(
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