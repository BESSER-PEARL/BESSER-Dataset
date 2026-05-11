





import java.util.List;
import java.util.ArrayList;

public class table_DFeatureColumn extends DColumn {

    private String featureName;



    public table_DFeatureColumn(
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