





import java.util.List;
import java.util.ArrayList;

public class hydraconstraints_SimpleFeature extends BoolOperandChoices {

    private String featureName;



    public hydraconstraints_SimpleFeature(
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