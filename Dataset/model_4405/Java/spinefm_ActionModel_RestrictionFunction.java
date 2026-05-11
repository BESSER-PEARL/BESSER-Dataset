





import java.util.List;
import java.util.ArrayList;

public class spinefm_ActionModel_RestrictionFunction  {

    private String id;





    private RestrictionFunction restrictionfunction;


    public spinefm_ActionModel_RestrictionFunction(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public RestrictionFunction getRestrictionfunction() {
        return restrictionfunction;
    }

    public void setRestrictionfunction(RestrictionFunction restrictionfunction) {
        this.restrictionfunction = restrictionfunction;
    }

}