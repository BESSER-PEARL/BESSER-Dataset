





import java.util.List;
import java.util.ArrayList;

public class core_BooleanLiteral extends Expression {

    private boolean value;



    public core_BooleanLiteral(
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