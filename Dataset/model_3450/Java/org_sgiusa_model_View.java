





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_View  {

    private String userId;
    private String viewType;
    private String id;





    private Organization organization;


    public org_sgiusa_model_View(
        String userId,        String viewType,        String id    ) {
        this.userId = userId;
        this.viewType = viewType;
        this.id = id;
    }


    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getViewtype() {
        return viewType;
    }

    public void setViewtype(String viewType) {
        this.viewType = viewType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}