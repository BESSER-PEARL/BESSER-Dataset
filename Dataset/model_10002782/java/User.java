





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String About;
    private String Facebook_link;
    private String Username;
    private String Linkedin_link;
    private String Position;
    private String Google_plus_link;
    private String Roles___;
    private String Firstname;
    private int DepartmentID;
    private int TitleID;
    private String Phone;
    private String Settings;
    private String Hiredate;
    private int UserID;
    private String Email;
    private String Password;
    private String Dateofbirth;
    private boolean Active;
    private String Lastname;



    public User(
        String About,        String Facebook_link,        String Username,        String Linkedin_link,        String Position,        String Google_plus_link,        String Roles___,        String Firstname,        int DepartmentID,        int TitleID,        String Phone,        String Settings,        String Hiredate,        int UserID,        String Email,        String Password,        String Dateofbirth,        boolean Active,        String Lastname    ) {
        this.About = About;
        this.Facebook_link = Facebook_link;
        this.Username = Username;
        this.Linkedin_link = Linkedin_link;
        this.Position = Position;
        this.Google_plus_link = Google_plus_link;
        this.Roles___ = Roles___;
        this.Firstname = Firstname;
        this.DepartmentID = DepartmentID;
        this.TitleID = TitleID;
        this.Phone = Phone;
        this.Settings = Settings;
        this.Hiredate = Hiredate;
        this.UserID = UserID;
        this.Email = Email;
        this.Password = Password;
        this.Dateofbirth = Dateofbirth;
        this.Active = Active;
        this.Lastname = Lastname;
    }


    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
    }
    public String getRoles___() {
        return Roles___;
    }

    public void setRoles___(String Roles___) {
        this.Roles___ = Roles___;
    }
    public String getFirstname() {
        return Firstname;
    }

    public void setFirstname(String Firstname) {
        this.Firstname = Firstname;
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
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
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
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }
    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public String getLastname() {
        return Lastname;
    }

    public void setLastname(String Lastname) {
        this.Lastname = Lastname;
    }


}