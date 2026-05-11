





import java.util.List;
import java.util.ArrayList;

public class SMTlib2extended_ConstBooleanExpression extends ConstExpression {

    private boolean value;



    public SMTlib2extended_ConstBooleanExpression(
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