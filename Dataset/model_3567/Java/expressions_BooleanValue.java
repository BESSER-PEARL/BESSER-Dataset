





import java.util.List;
import java.util.ArrayList;

public class expressions_BooleanValue extends SomeValue, LExpression {

    private boolean value;



    public expressions_BooleanValue(
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