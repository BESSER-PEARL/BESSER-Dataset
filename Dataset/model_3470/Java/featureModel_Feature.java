





import java.util.List;
import java.util.ArrayList;

public class featureModel_Feature  {

    private String type;
    private String name;





    private List<featureModel_SolitaryFeature> featuremodel_solitaryfeatures;


    public featureModel_Feature(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.featuremodel_solitaryfeatures = new ArrayList<>();
    }

    public featureModel_Feature(
        String type,        String name        ArrayList<featureModel_SolitaryFeature> featuremodel_solitaryfeatures    ) {
        this.type = type;
        this.name = name;
        this.featuremodel_solitaryfeatures = featuremodel_solitaryfeatures;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<featureModel_SolitaryFeature> getFeaturemodel_solitaryfeatures() {
        return featuremodel_solitaryfeatures;
    }

    public void addFeaturemodel_solitaryfeature(Featuremodel_solitaryfeature featuremodel_solitaryfeature) {
        this.featuremodel_solitaryfeatures.add(featuremodel_solitaryfeature);
    }

}