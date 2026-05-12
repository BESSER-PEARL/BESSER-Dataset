





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_StringVal extends Value {

    private String value;



    public SQLDDL_StringVal(
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