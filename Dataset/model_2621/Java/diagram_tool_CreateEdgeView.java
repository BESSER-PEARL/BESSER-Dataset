





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_CreateEdgeView extends CreateView {

    private String sourceExpression;
    private String targetExpression;



    public diagram_tool_CreateEdgeView(
        String sourceExpression,        String targetExpression    ) {
        super(
        );
        this.sourceExpression = sourceExpression;
        this.targetExpression = targetExpression;
    }


    public String getSourceexpression() {
        return sourceExpression;
    }

    public void setSourceexpression(String sourceExpression) {
        this.sourceExpression = sourceExpression;
    }
    public String getTargetexpression() {
        return targetExpression;
    }

    public void setTargetexpression(String targetExpression) {
        this.targetExpression = targetExpression;
    }


}