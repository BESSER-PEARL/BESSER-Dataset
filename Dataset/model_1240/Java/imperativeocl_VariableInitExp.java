





import java.util.List;
import java.util.ArrayList;

public class imperativeocl_VariableInitExp extends ImperativeExpression {

    private String withResult;



    public imperativeocl_VariableInitExp(
        String withResult    ) {
        super(
        );
        this.withResult = withResult;
    }


    public String getWithresult() {
        return withResult;
    }

    public void setWithresult(String withResult) {
        this.withResult = withResult;
    }


}