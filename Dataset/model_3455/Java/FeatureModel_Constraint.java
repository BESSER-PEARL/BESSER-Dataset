





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_Constraint extends NamedElement {

    private String language;
    private String code;





    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_Constraint(
        String language,        String code    ) {
        super(
        );
        this.language = language;
        this.code = code;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}