





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_SetObject extends ContainerModelOperation {

    private String featureName;



    public viewpoint_tool_SetObject(
        String featureName    ) {
        super(
        );
        this.featureName = featureName;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}