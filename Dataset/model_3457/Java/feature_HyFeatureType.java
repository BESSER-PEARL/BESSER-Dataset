





import java.util.List;
import java.util.ArrayList;

public class feature_HyFeatureType extends HyLinearTemporalElement {

    private String type;





    private feature_HyFeature feature_hyfeature;


    public feature_HyFeatureType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public feature_HyFeature getFeature_hyfeature() {
        return feature_hyfeature;
    }

    public void setFeature_hyfeature(feature_HyFeature feature_hyfeature) {
        this.feature_hyfeature = feature_hyfeature;
    }

}