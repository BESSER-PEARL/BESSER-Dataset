





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_BooleanValue extends PrimitiveValue {

    private boolean value;



    public fUML_Kernel_BooleanValue(
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