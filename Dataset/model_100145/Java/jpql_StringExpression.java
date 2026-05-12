





import java.util.List;
import java.util.ArrayList;

public class jpql_StringExpression extends Value {

    private String value;



    public jpql_StringExpression(
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