





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_NamedElement  {

    private String name;





    private FeatureModel_Comment featuremodel_comment;


    public FeatureModel_NamedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FeatureModel_Comment getFeaturemodel_comment() {
        return featuremodel_comment;
    }

    public void setFeaturemodel_comment(FeatureModel_Comment featuremodel_comment) {
        this.featuremodel_comment = featuremodel_comment;
    }

}