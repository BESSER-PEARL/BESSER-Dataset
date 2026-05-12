





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String User_Name;
    private String ID_Profile;
    private String About;
    private String Password;



    public Profile(
        String User_Name,        String ID_Profile,        String About,        String Password    ) {
        this.User_Name = User_Name;
        this.ID_Profile = ID_Profile;
        this.About = About;
        this.Password = Password;
    }


    public String getUser_name() {
        return User_Name;
    }

    public void setUser_name(String User_Name) {
        this.User_Name = User_Name;
    }
    public String getId_profile() {
        return ID_Profile;
    }

    public void setId_profile(String ID_Profile) {
        this.ID_Profile = ID_Profile;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}