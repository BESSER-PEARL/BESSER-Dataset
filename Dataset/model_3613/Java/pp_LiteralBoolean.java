





import java.util.List;
import java.util.ArrayList;

public class pp_LiteralBoolean extends LiteralExpression {

    private boolean value;



    public pp_LiteralBoolean(
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