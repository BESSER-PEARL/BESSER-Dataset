





import java.util.List;
import java.util.ArrayList;

public class JTL_imperativeocl_VariableInitExp extends ImperativeExpression {

    private boolean withResult;



    public JTL_imperativeocl_VariableInitExp(
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