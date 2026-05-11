





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_SetValue extends ContainerModelOperation {

    private String featureName;
    private String valueExpression;



    public viewpoint_tool_SetValue(
        String featureName,        String valueExpression    ) {
        super(
        );
        this.featureName = featureName;
        this.valueExpression = valueExpression;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getValueexpression() {
        return valueExpression;
    }

    public void setValueexpression(String valueExpression) {
        this.valueExpression = valueExpression;
    }


}