





import java.util.List;
import java.util.ArrayList;

public class xmof_Kernel_BooleanValue extends PrimitiveValue {

    private boolean value;



    public xmof_Kernel_BooleanValue(
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