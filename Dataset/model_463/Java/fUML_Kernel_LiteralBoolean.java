





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_LiteralBoolean extends LiteralSpecification {

    private boolean value;



    public fUML_Kernel_LiteralBoolean(
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