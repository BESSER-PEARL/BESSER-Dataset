





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_RealLiteralExp extends LiteralExp {

    private String value;



    public ir_ocl_RealLiteralExp(
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