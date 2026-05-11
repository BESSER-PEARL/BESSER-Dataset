





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ScreenModelParameter  {

    private String modelFeatureValue;





    private domainmodel_ModelFeature domainmodel_modelfeature;


    public domainmodel_ScreenModelParameter(
        String modelFeatureValue    ) {
        this.modelFeatureValue = modelFeatureValue;
    }


    public String getModelfeaturevalue() {
        return modelFeatureValue;
    }

    public void setModelfeaturevalue(String modelFeatureValue) {
        this.modelFeatureValue = modelFeatureValue;
    }

    public domainmodel_ModelFeature getDomainmodel_modelfeature() {
        return domainmodel_modelfeature;
    }

    public void setDomainmodel_modelfeature(domainmodel_ModelFeature domainmodel_modelfeature) {
        this.domainmodel_modelfeature = domainmodel_modelfeature;
    }

}