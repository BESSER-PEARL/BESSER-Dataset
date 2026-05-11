





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_AccessByFeatureOptimization extends QueueOptimization {

    private String featureName;
    private boolean force;



    public frontend_qool_AccessByFeatureOptimization(
        String featureName,        boolean force    ) {
        super(
        );
        this.featureName = featureName;
        this.force = force;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public boolean getForce() {
        return force;
    }

    public void setForce(boolean force) {
        this.force = force;
    }


}