





import java.util.List;
import java.util.ArrayList;

public class ir_IntegerLiteral extends LiteralExpression {

    private String value;



    public ir_IntegerLiteral(
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