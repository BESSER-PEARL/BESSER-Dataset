





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_BooleanLiteralExp extends LiteralExp {

    private boolean value;



    public ir_ocl_BooleanLiteralExp(
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