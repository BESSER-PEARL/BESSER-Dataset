





import java.util.List;
import java.util.ArrayList;

public class myDsl_booleanType extends type_specifier, simple_expression {

    private String bool_type;
    private String value;



    public myDsl_booleanType(
        String bool_type,        String value    ) {
        super(
        );
        this.bool_type = bool_type;
        this.value = value;
    }


    public String getBool_type() {
        return bool_type;
    }

    public void setBool_type(String bool_type) {
        this.bool_type = bool_type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}