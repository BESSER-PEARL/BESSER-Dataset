





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_VariableInitExp extends ImperativeExpression {

    private boolean withResult;



    public JTLMM_imperativeocl_VariableInitExp(
        boolean withResult    ) {
        super(
        );
        this.withResult = withResult;
    }


    public boolean getWithresult() {
        return withResult;
    }

    public void setWithresult(boolean withResult) {
        this.withResult = withResult;
    }


}