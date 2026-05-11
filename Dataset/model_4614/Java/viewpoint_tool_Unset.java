





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_Unset extends ContainerModelOperation {

    private String featureName;
    private String elementExpression;



    public viewpoint_tool_Unset(
        String featureName,        String elementExpression    ) {
        super(
        );
        this.featureName = featureName;
        this.elementExpression = elementExpression;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getElementexpression() {
        return elementExpression;
    }

    public void setElementexpression(String elementExpression) {
        this.elementExpression = elementExpression;
    }


}