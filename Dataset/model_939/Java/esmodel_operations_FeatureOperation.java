





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_FeatureOperation extends AbstractOperation {

    private String featureName;



    public esmodel_operations_FeatureOperation(
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