





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_IntegerVal extends Value {

    private String value;



    public SQLDDL_IntegerVal(
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