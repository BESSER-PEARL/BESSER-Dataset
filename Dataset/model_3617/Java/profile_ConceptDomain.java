





import java.util.List;
import java.util.ArrayList;

public class profile_ConceptDomain  {

    private String statusDate;
    private String status;
    private String fullName;
    private String identifier;





    private profile_ConceptDomainConstraint profile_conceptdomainconstraint;


    public profile_ConceptDomain(
        String statusDate,        String status,        String fullName,        String identifier    ) {
        this.statusDate = statusDate;
        this.status = status;
        this.fullName = fullName;
        this.identifier = identifier;
    }


    public String getStatusdate() {
        return statusDate;
    }

    public void setStatusdate(String statusDate) {
        this.statusDate = statusDate;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public profile_ConceptDomainConstraint getProfile_conceptdomainconstraint() {
        return profile_conceptdomainconstraint;
    }

    public void setProfile_conceptdomainconstraint(profile_ConceptDomainConstraint profile_conceptdomainconstraint) {
        this.profile_conceptdomainconstraint = profile_conceptdomainconstraint;
    }

}