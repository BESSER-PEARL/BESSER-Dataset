





import java.util.List;
import java.util.ArrayList;

public class statechartexpressions_LiteralValue extends PrimaryExpression {

    private String value;



    public statechartexpressions_LiteralValue(
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