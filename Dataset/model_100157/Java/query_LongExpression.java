





import java.util.List;
import java.util.ArrayList;

public class query_LongExpression extends Expression {

    private String value;



    public query_LongExpression(
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