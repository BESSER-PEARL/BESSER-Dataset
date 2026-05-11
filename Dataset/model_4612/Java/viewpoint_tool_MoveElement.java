





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_MoveElement extends ContainerModelOperation {

    private String featureName;
    private String newContainerExpression;



    public viewpoint_tool_MoveElement(
        String featureName,        String newContainerExpression    ) {
        super(
        );
        this.featureName = featureName;
        this.newContainerExpression = newContainerExpression;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public String getNewcontainerexpression() {
        return newContainerExpression;
    }

    public void setNewcontainerexpression(String newContainerExpression) {
        this.newContainerExpression = newContainerExpression;
    }


}