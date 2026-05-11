





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_CreateEdgeView extends CreateView {

    private String targetExpression;
    private String sourceExpression;



    public diagram_tool_CreateEdgeView(
        String targetExpression,        String sourceExpression    ) {
        super(
        );
        this.targetExpression = targetExpression;
        this.sourceExpression = sourceExpression;
    }


    public String getTargetexpression() {
        return targetExpression;
    }

    public void setTargetexpression(String targetExpression) {
        this.targetExpression = targetExpression;
    }
    public String getSourceexpression() {
        return sourceExpression;
    }

    public void setSourceexpression(String sourceExpression) {
        this.sourceExpression = sourceExpression;
    }


}