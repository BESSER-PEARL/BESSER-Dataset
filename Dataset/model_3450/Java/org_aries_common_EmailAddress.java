





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_EmailAddress  {

    private String lastName;
    private String id;
    private String enabled;
    private String userId;
    private String url;
    private String lastUpdate;
    private String creationDate;
    private String organization;
    private String firstName;



    public org_aries_common_EmailAddress(
        String lastName,        String id,        String enabled,        String userId,        String url,        String lastUpdate,        String creationDate,        String organization,        String firstName    ) {
        this.lastName = lastName;
        this.id = id;
        this.enabled = enabled;
        this.userId = userId;
        this.url = url;
        this.lastUpdate = lastUpdate;
        this.creationDate = creationDate;
        this.organization = organization;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}