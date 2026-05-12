





import java.util.List;
import java.util.ArrayList;

public class MavenProject_Person  {

    private String properties;
    private String url;
    private String name;
    private String timezone;
    private String email;
    private String organization;
    private String organizationUrl;
    private String roles;



    public MavenProject_Person(
        String properties,        String url,        String name,        String timezone,        String email,        String organization,        String organizationUrl,        String roles    ) {
        this.properties = properties;
        this.url = url;
        this.name = name;
        this.timezone = timezone;
        this.email = email;
        this.organization = organization;
        this.organizationUrl = organizationUrl;
        this.roles = roles;
    }


    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTimezone() {
        return timezone;
    }

    public void setTimezone(String timezone) {
        this.timezone = timezone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getOrganizationurl() {
        return organizationUrl;
    }

    public void setOrganizationurl(String organizationUrl) {
        this.organizationUrl = organizationUrl;
    }
    public String getRoles() {
        return roles;
    }

    public void setRoles(String roles) {
        this.roles = roles;
    }


}