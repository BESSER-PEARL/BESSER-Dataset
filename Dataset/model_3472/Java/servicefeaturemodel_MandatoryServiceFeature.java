





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_MandatoryServiceFeature extends ServiceFeature {

    private String featureTypes;



    public servicefeaturemodel_MandatoryServiceFeature(
        String featureTypes    ) {
        super(
        );
        this.featureTypes = featureTypes;
    }


    public String getFeaturetypes() {
        return featureTypes;
    }

    public void setFeaturetypes(String featureTypes) {
        this.featureTypes = featureTypes;
    }


}