





import java.util.List;
import java.util.ArrayList;

public class cloudml_RelationshipInstance extends CloudMLElementWithProperties {






    private cloudml_Relationship cloudml_relationship;




    private cloudml_CloudMLModel cloudml_cloudmlmodel;


    public cloudml_RelationshipInstance(
    ) {
        super(
        );
    }



    public cloudml_Relationship getCloudml_relationship() {
        return cloudml_relationship;
    }

    public void setCloudml_relationship(cloudml_Relationship cloudml_relationship) {
        this.cloudml_relationship = cloudml_relationship;
    }
    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }

}