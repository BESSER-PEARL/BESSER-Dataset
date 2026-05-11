





import java.util.List;
import java.util.ArrayList;

public class ca_rule_IntegerLiteral extends IntegerExpression {

    private int value;



    public ca_rule_IntegerLiteral(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}