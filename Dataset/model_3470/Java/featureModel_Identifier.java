





import java.util.List;
import java.util.ArrayList;

public class featureModel_Identifier extends Expression {

    private String name;





    private List<featureModel_Feature> featuremodel_features;


    public featureModel_Identifier(
        String name    ) {
        super(
        );
        this.name = name;
        this.featuremodel_features = new ArrayList<>();
    }

    public featureModel_Identifier(
        String name        ArrayList<featureModel_Feature> featuremodel_features    ) {
        this.name = name;
        this.featuremodel_features = featuremodel_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<featureModel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }

}