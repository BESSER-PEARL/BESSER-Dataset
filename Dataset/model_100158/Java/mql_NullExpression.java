





import java.util.List;
import java.util.ArrayList;

public class mql_NullExpression extends Value {

    private String value;



    public mql_NullExpression(
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