





import java.util.List;
import java.util.ArrayList;

public class mt_expressions_BooleanLiteral extends Literal {

    private boolean value;



    public mt_expressions_BooleanLiteral(
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