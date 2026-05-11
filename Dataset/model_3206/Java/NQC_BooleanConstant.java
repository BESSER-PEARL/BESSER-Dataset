





import java.util.List;
import java.util.ArrayList;

public class NQC_BooleanConstant extends ConstantExpression {

    private boolean Value;



    public NQC_BooleanConstant(
        boolean Value    ) {
        super(
        );
        this.Value = Value;
    }


    public boolean getValue() {
        return Value;
    }

    public void setValue(boolean Value) {
        this.Value = Value;
    }


}