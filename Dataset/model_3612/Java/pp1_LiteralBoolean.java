





import java.util.List;
import java.util.ArrayList;

public class pp1_LiteralBoolean extends LiteralExpression {

    private boolean value;



    public pp1_LiteralBoolean(
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