





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Linkedin_link;
    private String Lastname;
    private String Username;
    private String Settings;
    private String Email;
    private String Hiredate;
    private int DepartmentID;
    private String Firstname;
    private boolean Active;
    private String About;
    private String Facebook_link;
    private String Roles___;
    private String Google_plus_link;
    private String Password;
    private int UserID;
    private int TitleID;
    private String Phone;
    private String Position;
    private String Dateofbirth;



    public User(
        String Linkedin_link,        String Lastname,        String Username,        String Settings,        String Email,        String Hiredate,        int DepartmentID,        String Firstname,        boolean Active,        String About,        String Facebook_link,        String Roles___,        String Google_plus_link,        String Password,        int UserID,        int TitleID,        String Phone,        String Position,        String Dateofbirth    ) {
        this.Linkedin_link = Linkedin_link;
        this.Lastname = Lastname;
        this.Username = Username;
        this.Settings = Settings;
        this.Email = Email;
        this.Hiredate = Hiredate;
        this.DepartmentID = DepartmentID;
        this.Firstname = Firstname;
        this.Active = Active;
        this.About = About;
        this.Facebook_link = Facebook_link;
        this.Roles___ = Roles___;
        this.Google_plus_link = Google_plus_link;
        this.Password = Password;
        this.UserID = UserID;
        this.TitleID = TitleID;
        this.Phone = Phone;
        this.Position = Position;
        this.Dateofbirth = Dateofbirth;
    }


    public String getLinkedin_link() {
        return Linkedin_link;
    }

    public void setLinkedin_link(String Linkedin_link) {
        this.Linkedin_link = Linkedin_link;
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
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
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
    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
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
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getDateofbirth() {
        return Dateofbirth;
    }

    public void setDateofbirth(String Dateofbirth) {
        this.Dateofbirth = Dateofbirth;
    }


}