





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_VariableInitExp extends ImperativeExpression {

    private String withResult;



    public FlatQVT_VariableInitExp(
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