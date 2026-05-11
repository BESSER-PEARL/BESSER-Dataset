





import java.util.List;
import java.util.ArrayList;

public class cloudml_RequiredPort extends Port {

    private boolean isMandatory;





    private cloudml_InternalComponent cloudml_internalcomponent;




    private cloudml_Relationship cloudml_relationship;


    public cloudml_RequiredPort(
        boolean isMandatory    ) {
        super(
        );
        this.isMandatory = isMandatory;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }

    public cloudml_InternalComponent getCloudml_internalcomponent() {
        return cloudml_internalcomponent;
    }

    public void setCloudml_internalcomponent(cloudml_InternalComponent cloudml_internalcomponent) {
        this.cloudml_internalcomponent = cloudml_internalcomponent;
    }
    public cloudml_Relationship getCloudml_relationship() {
        return cloudml_relationship;
    }

    public void setCloudml_relationship(cloudml_Relationship cloudml_relationship) {
        this.cloudml_relationship = cloudml_relationship;
    }

}