





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Organization  {

    private String level;
    private String lastUpdate;
    private String abbrv;
    private String label;
    private String type;
    private String id;
    private String creationDate;
    private String permissionId;
    private String name;
    private String zipCodes;
    private String organizationId;





    private List<Organization> organizations;




    private Organization organization;




    private User user;




    private List<User> users;




    private User user;


    public org_sgiusa_model_Organization(
        String level,        String lastUpdate,        String abbrv,        String label,        String type,        String id,        String creationDate,        String permissionId,        String name,        String zipCodes,        String organizationId    ) {
        this.level = level;
        this.lastUpdate = lastUpdate;
        this.abbrv = abbrv;
        this.label = label;
        this.type = type;
        this.id = id;
        this.creationDate = creationDate;
        this.permissionId = permissionId;
        this.name = name;
        this.zipCodes = zipCodes;
        this.organizationId = organizationId;
        this.organizations = new ArrayList<>();
        this.users = new ArrayList<>();
    }

    public org_sgiusa_model_Organization(
        String level,        String lastUpdate,        String abbrv,        String label,        String type,        String id,        String creationDate,        String permissionId,        String name,        String zipCodes,        String organizationId        ArrayList<Organization> organizations,        ArrayList<User> users    ) {
        this.level = level;
        this.lastUpdate = lastUpdate;
        this.abbrv = abbrv;
        this.label = label;
        this.type = type;
        this.id = id;
        this.creationDate = creationDate;
        this.permissionId = permissionId;
        this.name = name;
        this.zipCodes = zipCodes;
        this.organizationId = organizationId;
        this.organizations = organizations;
        this.users = users;
    }

    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getAbbrv() {
        return abbrv;
    }

    public void setAbbrv(String abbrv) {
        this.abbrv = abbrv;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getPermissionid() {
        return permissionId;
    }

    public void setPermissionid(String permissionId) {
        this.permissionId = permissionId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getZipcodes() {
        return zipCodes;
    }

    public void setZipcodes(String zipCodes) {
        this.zipCodes = zipCodes;
    }
    public String getOrganizationid() {
        return organizationId;
    }

    public void setOrganizationid(String organizationId) {
        this.organizationId = organizationId;
    }

    public List<Organization> getOrganizations() {
        return organizations;
    }

    public void addOrganization(Organization organization) {
        this.organizations.add(organization);
    }
    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}