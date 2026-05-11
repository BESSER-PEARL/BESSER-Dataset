





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_StringLiteral extends ScalarExpression, Expression {

    private String value;



    public applauseDsl_StringLiteral(
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