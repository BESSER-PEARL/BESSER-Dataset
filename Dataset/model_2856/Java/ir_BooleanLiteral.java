





import java.util.List;
import java.util.ArrayList;

public class ir_BooleanLiteral extends LiteralExpression {

    private boolean value;



    public ir_BooleanLiteral(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}