





import java.util.List;
import java.util.ArrayList;

public class cal_AstExpressionBoolean extends AstExpressionLiteral {

    private boolean value;



    public cal_AstExpressionBoolean(
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