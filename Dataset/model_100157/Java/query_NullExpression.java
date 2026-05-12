





import java.util.List;
import java.util.ArrayList;

public class query_NullExpression extends Expression {

    private String value;



    public query_NullExpression(
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