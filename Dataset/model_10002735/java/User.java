





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Google_plus_link;
    private String Linkedin_link;
    private String Position;
    private String Hiredate;
    private String Firstname;
    private String Facebook_link;
    private String Email;
    private String Settings;
    private String Dateofbirth;
    private String Password;
    private String Username;
    private String About;
    private int TitleID;
    private String Roles___;
    private int UserID;
    private String Phone;
    private int DepartmentID;
    private boolean Active;
    private String Lastname;



    public User(
        String Google_plus_link,        String Linkedin_link,        String Position,        String Hiredate,        String Firstname,        String Facebook_link,        String Email,        String Settings,        String Dateofbirth,        String Password,        String Username,        String About,        int TitleID,        String Roles___,        int UserID,        String Phone,        int DepartmentID,        boolean Active,        String Lastname    ) {
        this.Google_plus_link = Google_plus_link;
        this.Linkedin_link = Linkedin_link;
        this.Position = Position;
        this.Hiredate = Hiredate;
        this.Firstname = Firstname;
        this.Facebook_link = Facebook_link;
        this.Email = Email;
        this.Settings = Settings;
        this.Dateofbirth = Dateofbirth;
        this.Password = Password;
        this.Username = Username;
        this.About = About;
        this.TitleID = TitleID;
        this.Roles___ = Roles___;
        this.UserID = UserID;
        this.Phone = Phone;
        this.DepartmentID = DepartmentID;
        this.Active = Active;
        this.Lastname = Lastname;
    }


    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
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
    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }
    public String getFirstname() {
        return Firstname;
    }

    public void setFirstname(String Firstname) {
        this.Firstname = Firstname;
    }
    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
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
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
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
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public String getRoles___() {
        return Roles___;
    }

    public void setRoles___(String Roles___) {
        this.Roles___ = Roles___;
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
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
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