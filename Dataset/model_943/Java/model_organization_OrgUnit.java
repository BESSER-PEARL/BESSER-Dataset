





import java.util.List;
import java.util.ArrayList;

public class model_organization_OrgUnit extends UnicaseModelElement {

    private String acOrgId;



    public model_organization_OrgUnit(
        String acOrgId    ) {
        super(
        );
        this.acOrgId = acOrgId;
    }


    public String getAcorgid() {
        return acOrgId;
    }

    public void setAcorgid(String acOrgId) {
        this.acOrgId = acOrgId;
    }


}