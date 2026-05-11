





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_AcceleoVariable extends tool_SubVariable, tool_VariableContainer {

    private String computationExpression;



    public viewpoint_tool_AcceleoVariable(
        String computationExpression    ) {
        super(
        );
        this.computationExpression = computationExpression;
    }


    public String getComputationexpression() {
        return computationExpression;
    }

    public void setComputationexpression(String computationExpression) {
        this.computationExpression = computationExpression;
    }


}