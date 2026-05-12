





import java.util.List;
import java.util.ArrayList;

public class jPQL_BooleanExpression extends Value {

    private boolean value;



    public jPQL_BooleanExpression(
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