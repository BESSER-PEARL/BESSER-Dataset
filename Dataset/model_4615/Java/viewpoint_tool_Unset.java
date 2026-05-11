





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_Unset extends ContainerModelOperation {

    private String elementExpression;
    private String featureName;



    public viewpoint_tool_Unset(
        String elementExpression,        String featureName    ) {
        super(
        );
        this.elementExpression = elementExpression;
        this.featureName = featureName;
    }


    public String getElementexpression() {
        return elementExpression;
    }

    public void setElementexpression(String elementExpression) {
        this.elementExpression = elementExpression;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}