





import java.util.List;
import java.util.ArrayList;

public class pp2_LiteralBoolean extends LiteralExpression {

    private boolean value;



    public pp2_LiteralBoolean(
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