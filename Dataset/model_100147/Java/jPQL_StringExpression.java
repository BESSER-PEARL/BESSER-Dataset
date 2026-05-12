





import java.util.List;
import java.util.ArrayList;

public class jPQL_StringExpression extends Value {

    private String value;



    public jPQL_StringExpression(
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