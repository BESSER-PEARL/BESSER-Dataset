





import java.util.List;
import java.util.ArrayList;

public class application_OCLRestrictedProperty extends Property {

    private String OCLRestriction;



    public application_OCLRestrictedProperty(
        String OCLRestriction    ) {
        super(
        );
        this.OCLRestriction = OCLRestriction;
    }


    public String getOclrestriction() {
        return OCLRestriction;
    }

    public void setOclrestriction(String OCLRestriction) {
        this.OCLRestriction = OCLRestriction;
    }


}