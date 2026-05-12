





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Google_plus_link;
    private String Password;
    private String Linkedin_link;
    private String Phone;
    private String Lastname;
    private String Username;
    private int DepartmentID;
    private int TitleID;
    private String Email;
    private int UserID;
    private String Dateofbirth;
    private String Hiredate;
    private String About;
    private String Firstname;
    private String Settings;
    private boolean Active;
    private String Roles___;
    private String Facebook_link;
    private String Position;



    public User(
        String Google_plus_link,        String Password,        String Linkedin_link,        String Phone,        String Lastname,        String Username,        int DepartmentID,        int TitleID,        String Email,        int UserID,        String Dateofbirth,        String Hiredate,        String About,        String Firstname,        String Settings,        boolean Active,        String Roles___,        String Facebook_link,        String Position    ) {
        this.Google_plus_link = Google_plus_link;
        this.Password = Password;
        this.Linkedin_link = Linkedin_link;
        this.Phone = Phone;
        this.Lastname = Lastname;
        this.Username = Username;
        this.DepartmentID = DepartmentID;
        this.TitleID = TitleID;
        this.Email = Email;
        this.UserID = UserID;
        this.Dateofbirth = Dateofbirth;
        this.Hiredate = Hiredate;
        this.About = About;
        this.Firstname = Firstname;
        this.Settings = Settings;
        this.Active = Active;
        this.Roles___ = Roles___;
        this.Facebook_link = Facebook_link;
        this.Position = Position;
    }


    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getLastname() {
        return Lastname;
    }

    public void setLastname(String Lastname) {
        this.Lastname = Lastname;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }
    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getFirstname() {
        return Firstname;
    }

    public void setFirstname(String Firstname) {
        this.Firstname = Firstname;
    }
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
    }
    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public String getRoles___() {
        return Roles___;
    }

    public void setRoles___(String Roles___) {
        this.Roles___ = Roles___;
    }
    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }


}