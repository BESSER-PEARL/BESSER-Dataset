





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_AccessByFeatureOptimization extends QueueOptimization {

    private boolean force;
    private String featureName;



    public frontend_qool_AccessByFeatureOptimization(
        boolean force,        String featureName    ) {
        super(
        );
        this.force = force;
        this.featureName = featureName;
    }


    public boolean getForce() {
        return force;
    }

    public void setForce(boolean force) {
        this.force = force;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}