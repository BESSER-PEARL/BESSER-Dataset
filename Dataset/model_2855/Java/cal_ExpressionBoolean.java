





import java.util.List;
import java.util.ArrayList;

public class cal_ExpressionBoolean extends ExpressionLiteral {

    private boolean value;



    public cal_ExpressionBoolean(
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