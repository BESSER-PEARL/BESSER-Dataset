





import java.util.List;
import java.util.ArrayList;

public class morel_FeaturePathExp extends CallPathExp {

    private String feature;



    public morel_FeaturePathExp(
        String feature    ) {
        super(
        );
        this.feature = feature;
    }


    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }


}