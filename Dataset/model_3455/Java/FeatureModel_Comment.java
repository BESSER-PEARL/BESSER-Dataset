





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Comment extends NamedElement {

    private String text;





    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_Comment(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}