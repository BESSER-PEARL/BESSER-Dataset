





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Event  {

    private String subDivisions;
    private String userId;
    private String status;
    private String id;
    private String divisions;





    private Organization organization;


    public org_sgiusa_model_Event(
        String subDivisions,        String userId,        String status,        String id,        String divisions    ) {
        this.subDivisions = subDivisions;
        this.userId = userId;
        this.status = status;
        this.id = id;
        this.divisions = divisions;
    }


    public String getSubdivisions() {
        return subDivisions;
    }

    public void setSubdivisions(String subDivisions) {
        this.subDivisions = subDivisions;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDivisions() {
        return divisions;
    }

    public void setDivisions(String divisions) {
        this.divisions = divisions;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}