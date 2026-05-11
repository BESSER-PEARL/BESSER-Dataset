





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_User  {

    private String userId;
    private String lastName;
    private String role;
    private String firstName;
    private String enabled;
    private String id;
    private String password;





    private List<Permission> permissions;




    private StreetAddress streetaddress;




    private PhoneNumber phonenumber;




    private PhoneNumber phonenumber;




    private EmailAddress emailaddress;




    private Preferences preferences;




    private EmailAccount emailaccount;


    public org_sgiusa_model_User(
        String userId,        String lastName,        String role,        String firstName,        String enabled,        String id,        String password    ) {
        this.userId = userId;
        this.lastName = lastName;
        this.role = role;
        this.firstName = firstName;
        this.enabled = enabled;
        this.id = id;
        this.password = password;
        this.permissions = new ArrayList<>();
    }

    public org_sgiusa_model_User(
        String userId,        String lastName,        String role,        String firstName,        String enabled,        String id,        String password        ArrayList<Permission> permissions    ) {
        this.userId = userId;
        this.lastName = lastName;
        this.role = role;
        this.firstName = firstName;
        this.enabled = enabled;
        this.id = id;
        this.password = password;
        this.permissions = permissions;
    }

    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<Permission> getPermissions() {
        return permissions;
    }

    public void addPermission(Permission permission) {
        this.permissions.add(permission);
    }
    public StreetAddress getStreetaddress() {
        return streetaddress;
    }

    public void setStreetaddress(StreetAddress streetaddress) {
        this.streetaddress = streetaddress;
    }
    public PhoneNumber getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(PhoneNumber phonenumber) {
        this.phonenumber = phonenumber;
    }
    public PhoneNumber getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(PhoneNumber phonenumber) {
        this.phonenumber = phonenumber;
    }
    public EmailAddress getEmailaddress() {
        return emailaddress;
    }

    public void setEmailaddress(EmailAddress emailaddress) {
        this.emailaddress = emailaddress;
    }
    public Preferences getPreferences() {
        return preferences;
    }

    public void setPreferences(Preferences preferences) {
        this.preferences = preferences;
    }
    public EmailAccount getEmailaccount() {
        return emailaccount;
    }

    public void setEmailaccount(EmailAccount emailaccount) {
        this.emailaccount = emailaccount;
    }

}