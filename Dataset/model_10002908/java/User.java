





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Hiredate;
    private boolean Active;
    private String About;
    private String Username;
    private String Position;
    private String Settings;
    private String Roles___;
    private String Facebook_link;
    private String Email;
    private int DepartmentID;
    private String Lastname;
    private int UserID;
    private String Phone;
    private String Linkedin_link;
    private String Google_plus_link;
    private String Password;
    private int TitleID;
    private String Dateofbirth;
    private String Firstname;



    public User(
        String Hiredate,        boolean Active,        String About,        String Username,        String Position,        String Settings,        String Roles___,        String Facebook_link,        String Email,        int DepartmentID,        String Lastname,        int UserID,        String Phone,        String Linkedin_link,        String Google_plus_link,        String Password,        int TitleID,        String Dateofbirth,        String Firstname    ) {
        this.Hiredate = Hiredate;
        this.Active = Active;
        this.About = About;
        this.Username = Username;
        this.Position = Position;
        this.Settings = Settings;
        this.Roles___ = Roles___;
        this.Facebook_link = Facebook_link;
        this.Email = Email;
        this.DepartmentID = DepartmentID;
        this.Lastname = Lastname;
        this.UserID = UserID;
        this.Phone = Phone;
        this.Linkedin_link = Linkedin_link;
        this.Google_plus_link = Google_plus_link;
        this.Password = Password;
        this.TitleID = TitleID;
        this.Dateofbirth = Dateofbirth;
        this.Firstname = Firstname;
    }


    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }
    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
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
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
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
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
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
    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
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
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }
    public String getFirstname() {
        return Firstname;
    }

    public void setFirstname(String Firstname) {
        this.Firstname = Firstname;
    }


}