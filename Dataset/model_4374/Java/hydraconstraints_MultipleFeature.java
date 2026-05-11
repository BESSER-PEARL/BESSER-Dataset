





import java.util.List;
import java.util.ArrayList;

public class hydraconstraints_MultipleFeature extends NumOperandChoices {

    private String featureName;



    public hydraconstraints_MultipleFeature(
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