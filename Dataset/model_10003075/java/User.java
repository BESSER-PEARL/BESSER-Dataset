





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Lastname;
    private String Position;
    private String Linkedin_link;
    private int DepartmentID;
    private String Firstname;
    private String Google_plus_link;
    private boolean Active;
    private String Password;
    private int UserID;
    private int TitleID;
    private String Username;
    private String Phone;
    private String Facebook_link;
    private String About;
    private String Email;
    private String Dateofbirth;
    private String Settings;
    private String Hiredate;
    private String Roles___;



    public User(
        String Lastname,        String Position,        String Linkedin_link,        int DepartmentID,        String Firstname,        String Google_plus_link,        boolean Active,        String Password,        int UserID,        int TitleID,        String Username,        String Phone,        String Facebook_link,        String About,        String Email,        String Dateofbirth,        String Settings,        String Hiredate,        String Roles___    ) {
        this.Lastname = Lastname;
        this.Position = Position;
        this.Linkedin_link = Linkedin_link;
        this.DepartmentID = DepartmentID;
        this.Firstname = Firstname;
        this.Google_plus_link = Google_plus_link;
        this.Active = Active;
        this.Password = Password;
        this.UserID = UserID;
        this.TitleID = TitleID;
        this.Username = Username;
        this.Phone = Phone;
        this.Facebook_link = Facebook_link;
        this.About = About;
        this.Email = Email;
        this.Dateofbirth = Dateofbirth;
        this.Settings = Settings;
        this.Hiredate = Hiredate;
        this.Roles___ = Roles___;
    }


    public String getLastname() {
        return Lastname;
    }

    public void setLastname(String Lastname) {
        this.Lastname = Lastname;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
    }
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }
    public String getFirstname() {
        return Firstname;
    }

    public void setFirstname(String Firstname) {
        this.Firstname = Firstname;
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
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
    }
    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }
    public String getRoles___() {
        return Roles___;
    }

    public void setRoles___(String Roles___) {
        this.Roles___ = Roles___;
    }


}