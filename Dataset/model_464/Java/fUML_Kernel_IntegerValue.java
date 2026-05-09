





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_IntegerValue extends PrimitiveValue {

    private int value;



    public fUML_Kernel_IntegerValue(
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