





import java.util.List;
import java.util.ArrayList;

public class myDsl_intType extends type_specifier, simple_expression {

    private String int_type;
    private String value;



    public myDsl_intType(
        String int_type,        String value    ) {
        super(
        );
        this.int_type = int_type;
        this.value = value;
    }


    public String getInt_type() {
        return int_type;
    }

    public void setInt_type(String int_type) {
        this.int_type = int_type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}