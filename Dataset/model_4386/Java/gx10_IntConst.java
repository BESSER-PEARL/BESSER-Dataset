





import java.util.List;
import java.util.ArrayList;

public class gx10_IntConst extends IntExpression {

    private boolean value;



    public gx10_IntConst(
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