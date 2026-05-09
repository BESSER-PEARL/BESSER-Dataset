





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_BooleanValue extends PrimitiveValue {

    private boolean value;



    public fuml_Kernel_BooleanValue(
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