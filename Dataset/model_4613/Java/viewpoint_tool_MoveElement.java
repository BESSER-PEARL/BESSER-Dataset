





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_MoveElement extends ContainerModelOperation {

    private String newContainerExpression;
    private String featureName;



    public viewpoint_tool_MoveElement(
        String newContainerExpression,        String featureName    ) {
        super(
        );
        this.newContainerExpression = newContainerExpression;
        this.featureName = featureName;
    }


    public String getNewcontainerexpression() {
        return newContainerExpression;
    }

    public void setNewcontainerexpression(String newContainerExpression) {
        this.newContainerExpression = newContainerExpression;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}