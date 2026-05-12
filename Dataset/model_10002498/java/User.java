





import java.util.List;
import java.util.ArrayList;

public class User  {

    private boolean Active;
    private int DepartmentID;
    private int UserID;
    private String Google_plus_link;
    private String Hiredate;
    private String Firstname;
    private int TitleID;
    private String Lastname;
    private String Roles___;
    private String Facebook_link;
    private String Phone;
    private String Username;
    private String Linkedin_link;
    private String Settings;
    private String Position;
    private String Email;
    private String Password;
    private String About;
    private String Dateofbirth;



    public User(
        boolean Active,        int DepartmentID,        int UserID,        String Google_plus_link,        String Hiredate,        String Firstname,        int TitleID,        String Lastname,        String Roles___,        String Facebook_link,        String Phone,        String Username,        String Linkedin_link,        String Settings,        String Position,        String Email,        String Password,        String About,        String Dateofbirth    ) {
        this.Active = Active;
        this.DepartmentID = DepartmentID;
        this.UserID = UserID;
        this.Google_plus_link = Google_plus_link;
        this.Hiredate = Hiredate;
        this.Firstname = Firstname;
        this.TitleID = TitleID;
        this.Lastname = Lastname;
        this.Roles___ = Roles___;
        this.Facebook_link = Facebook_link;
        this.Phone = Phone;
        this.Username = Username;
        this.Linkedin_link = Linkedin_link;
        this.Settings = Settings;
        this.Position = Position;
        this.Email = Email;
        this.Password = Password;
        this.About = About;
        this.Dateofbirth = Dateofbirth;
    }


    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
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
    public int getTitleid() {
        return TitleID;
    }

    public void setTitleid(int TitleID) {
        this.TitleID = TitleID;
    }
    public String getLastname() {
        return Lastname;
    }

    public void setLastname(String Lastname) {
        this.Lastname = Lastname;
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
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
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
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
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
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }


}