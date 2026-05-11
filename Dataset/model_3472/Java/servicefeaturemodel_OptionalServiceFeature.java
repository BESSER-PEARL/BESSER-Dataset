





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_OptionalServiceFeature extends ServiceFeature {

    private String featureType;





    private servicefeaturemodel_GroupRelationship servicefeaturemodel_grouprelationship;


    public servicefeaturemodel_OptionalServiceFeature(
        String featureType    ) {
        super(
        );
        this.featureType = featureType;
    }


    public String getFeaturetype() {
        return featureType;
    }

    public void setFeaturetype(String featureType) {
        this.featureType = featureType;
    }

    public servicefeaturemodel_GroupRelationship getServicefeaturemodel_grouprelationship() {
        return servicefeaturemodel_grouprelationship;
    }

    public void setServicefeaturemodel_grouprelationship(servicefeaturemodel_GroupRelationship servicefeaturemodel_grouprelationship) {
        this.servicefeaturemodel_grouprelationship = servicefeaturemodel_grouprelationship;
    }

}