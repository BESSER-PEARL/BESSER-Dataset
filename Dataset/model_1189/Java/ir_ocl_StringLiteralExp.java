





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_StringLiteralExp extends LiteralExp {

    private String value;



    public ir_ocl_StringLiteralExp(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}