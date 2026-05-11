





import java.util.List;
import java.util.ArrayList;

public class workflow_TransformationTask extends WorkflowNode {

    private String transformExpression;



    public workflow_TransformationTask(
        String transformExpression    ) {
        super(
        );
        this.transformExpression = transformExpression;
    }


    public String getTransformexpression() {
        return transformExpression;
    }

    public void setTransformexpression(String transformExpression) {
        this.transformExpression = transformExpression;
    }


}