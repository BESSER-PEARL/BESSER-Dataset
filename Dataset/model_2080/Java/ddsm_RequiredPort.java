





import java.util.List;
import java.util.ArrayList;

public class ddsm_RequiredPort extends Port {

    private boolean isMandatory;





    private ddsm_InternalComponent ddsm_internalcomponent;




    private ddsm_Relationship ddsm_relationship;


    public ddsm_RequiredPort(
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

    public ddsm_InternalComponent getDdsm_internalcomponent() {
        return ddsm_internalcomponent;
    }

    public void setDdsm_internalcomponent(ddsm_InternalComponent ddsm_internalcomponent) {
        this.ddsm_internalcomponent = ddsm_internalcomponent;
    }
    public ddsm_Relationship getDdsm_relationship() {
        return ddsm_relationship;
    }

    public void setDdsm_relationship(ddsm_Relationship ddsm_relationship) {
        this.ddsm_relationship = ddsm_relationship;
    }

}