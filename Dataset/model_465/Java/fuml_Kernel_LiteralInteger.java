





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_LiteralInteger extends LiteralSpecification {

    private int value;



    public fuml_Kernel_LiteralInteger(
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