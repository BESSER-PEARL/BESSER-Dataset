





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Dateofbirth;
    private boolean Active;
    private String Hiredate;
    private String Username;
    private String Position;
    private int TitleID;
    private int DepartmentID;
    private String Lastname;
    private String Linkedin_link;
    private String Facebook_link;
    private String About;
    private String Email;
    private String Password;
    private int UserID;
    private String Roles___;
    private String Firstname;
    private String Settings;
    private String Google_plus_link;
    private String Phone;



    public User(
        String Dateofbirth,        boolean Active,        String Hiredate,        String Username,        String Position,        int TitleID,        int DepartmentID,        String Lastname,        String Linkedin_link,        String Facebook_link,        String About,        String Email,        String Password,        int UserID,        String Roles___,        String Firstname,        String Settings,        String Google_plus_link,        String Phone    ) {
        this.Dateofbirth = Dateofbirth;
        this.Active = Active;
        this.Hiredate = Hiredate;
        this.Username = Username;
        this.Position = Position;
        this.TitleID = TitleID;
        this.DepartmentID = DepartmentID;
        this.Lastname = Lastname;
        this.Linkedin_link = Linkedin_link;
        this.Facebook_link = Facebook_link;
        this.About = About;
        this.Email = Email;
        this.Password = Password;
        this.UserID = UserID;
        this.Roles___ = Roles___;
        this.Firstname = Firstname;
        this.Settings = Settings;
        this.Google_plus_link = Google_plus_link;
        this.Phone = Phone;
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
    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }
    public String getLastname() {
        return Lastname;
    }

    public void setLastname(String Lastname) {
        this.Lastname = Lastname;
    }
    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
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
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
    }
    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }


}