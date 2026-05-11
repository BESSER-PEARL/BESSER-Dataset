





import java.util.List;
import java.util.ArrayList;

public class myDsl_floatType extends type_specifier, simple_expression {

    private String float_type;
    private String value;



    public myDsl_floatType(
        String float_type,        String value    ) {
        super(
        );
        this.float_type = float_type;
        this.value = value;
    }


    public String getFloat_type() {
        return float_type;
    }

    public void setFloat_type(String float_type) {
        this.float_type = float_type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}