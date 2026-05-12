





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Google_plus_link;
    private String Facebook_link;
    private int DepartmentID;
    private boolean Active;
    private String Phone;
    private String About;
    private String Position;
    private String Roles___;
    private int TitleID;
    private String Lastname;
    private String Settings;
    private int UserID;
    private String Dateofbirth;
    private String Email;
    private String Linkedin_link;
    private String Firstname;
    private String Username;
    private String Hiredate;
    private String Password;



    public User(
        String Google_plus_link,        String Facebook_link,        int DepartmentID,        boolean Active,        String Phone,        String About,        String Position,        String Roles___,        int TitleID,        String Lastname,        String Settings,        int UserID,        String Dateofbirth,        String Email,        String Linkedin_link,        String Firstname,        String Username,        String Hiredate,        String Password    ) {
        this.Google_plus_link = Google_plus_link;
        this.Facebook_link = Facebook_link;
        this.DepartmentID = DepartmentID;
        this.Active = Active;
        this.Phone = Phone;
        this.About = About;
        this.Position = Position;
        this.Roles___ = Roles___;
        this.TitleID = TitleID;
        this.Lastname = Lastname;
        this.Settings = Settings;
        this.UserID = UserID;
        this.Dateofbirth = Dateofbirth;
        this.Email = Email;
        this.Linkedin_link = Linkedin_link;
        this.Firstname = Firstname;
        this.Username = Username;
        this.Hiredate = Hiredate;
        this.Password = Password;
    }


    public String getGoogle_plus_link() {
        return Google_plus_link;
    }

    public void setGoogle_plus_link(String Google_plus_link) {
        this.Google_plus_link = Google_plus_link;
    }
    public String getFacebook_link() {
        return Facebook_link;
    }

    public void setFacebook_link(String Facebook_link) {
        this.Facebook_link = Facebook_link;
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
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getRoles___() {
        return Roles___;
    }

    public void setRoles___(String Roles___) {
        this.Roles___ = Roles___;
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
    public String getSettings() {
        return Settings;
    }

    public void setSettings(String Settings) {
        this.Settings = Settings;
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
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
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
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getHiredate() {
        return Hiredate;
    }

    public void setHiredate(String Hiredate) {
        this.Hiredate = Hiredate;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}