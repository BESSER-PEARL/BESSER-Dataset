





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Facebook_link;
    private String Lastname;
    private int DepartmentID;
    private String Position;
    private String Password;
    private String Roles___;
    private String Google_plus_link;
    private boolean Active;
    private int UserID;
    private String Phone;
    private int TitleID;
    private String Settings;
    private String Dateofbirth;
    private String Username;
    private String About;
    private String Linkedin_link;
    private String Firstname;
    private String Email;
    private String Hiredate;





    private List<Role> roles;




    private List<Comment> comments;




    private List<Attachment> attachments;


    public User(
        String Facebook_link,        String Lastname,        int DepartmentID,        String Position,        String Password,        String Roles___,        String Google_plus_link,        boolean Active,        int UserID,        String Phone,        int TitleID,        String Settings,        String Dateofbirth,        String Username,        String About,        String Linkedin_link,        String Firstname,        String Email,        String Hiredate    ) {
        this.Facebook_link = Facebook_link;
        this.Lastname = Lastname;
        this.DepartmentID = DepartmentID;
        this.Position = Position;
        this.Password = Password;
        this.Roles___ = Roles___;
        this.Google_plus_link = Google_plus_link;
        this.Active = Active;
        this.UserID = UserID;
        this.Phone = Phone;
        this.TitleID = TitleID;
        this.Settings = Settings;
        this.Dateofbirth = Dateofbirth;
        this.Username = Username;
        this.About = About;
        this.Linkedin_link = Linkedin_link;
        this.Firstname = Firstname;
        this.Email = Email;
        this.Hiredate = Hiredate;
        this.roles = new ArrayList<>();
        this.comments = new ArrayList<>();
        this.attachments = new ArrayList<>();
    }

    public User(
        String Facebook_link,        String Lastname,        int DepartmentID,        String Position,        String Password,        String Roles___,        String Google_plus_link,        boolean Active,        int UserID,        String Phone,        int TitleID,        String Settings,        String Dateofbirth,        String Username,        String About,        String Linkedin_link,        String Firstname,        String Email,        String Hiredate        ArrayList<Role> roles,        ArrayList<Comment> comments,        ArrayList<Attachment> attachments    ) {
        this.Facebook_link = Facebook_link;
        this.Lastname = Lastname;
        this.DepartmentID = DepartmentID;
        this.Position = Position;
        this.Password = Password;
        this.Roles___ = Roles___;
        this.Google_plus_link = Google_plus_link;
        this.Active = Active;
        this.UserID = UserID;
        this.Phone = Phone;
        this.TitleID = TitleID;
        this.Settings = Settings;
        this.Dateofbirth = Dateofbirth;
        this.Username = Username;
        this.About = About;
        this.Linkedin_link = Linkedin_link;
        this.Firstname = Firstname;
        this.Email = Email;
        this.Hiredate = Hiredate;
        this.roles = roles;
        this.comments = comments;
        this.attachments = attachments;
    }

    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
    }
    public String getLastname() {
        return Lastname;
    }

    public void setLastname(String Lastname) {
        this.Lastname = Lastname;
    }
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getRoles___() {
        return Roles___;
    }

    public void setRoles___(String Roles___) {
        this.Roles___ = Roles___;
    }
    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
    }
    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
    }
    public String getFirstname() {
        return Firstname;
    }

    public void setFirstname(String Firstname) {
        this.Firstname = Firstname;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }

    public List<Role> getRoles() {
        return roles;
    }

    public void addRole(Role role) {
        this.roles.add(role);
    }
    public List<Comment> getComments() {
        return comments;
    }

    public void addComment(Comment comment) {
        this.comments.add(comment);
    }
    public List<Attachment> getAttachments() {
        return attachments;
    }

    public void addAttachment(Attachment attachment) {
        this.attachments.add(attachment);
    }

}