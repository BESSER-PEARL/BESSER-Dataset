





import java.util.List;
import java.util.ArrayList;

public class noop_BoolLiteral extends Expression {

    private boolean value;



    public noop_BoolLiteral(
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