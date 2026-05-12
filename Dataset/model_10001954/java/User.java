





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int ID_User;
    private String Name;
    private String Mail;
    private String Fist_Name;





    private Profile profile;


    public User(
        int ID_User,        String Name,        String Mail,        String Fist_Name    ) {
        this.ID_User = ID_User;
        this.Name = Name;
        this.Mail = Mail;
        this.Fist_Name = Fist_Name;
    }


    public int getId_user() {
        return ID_User;
    }

    public void setId_user(int ID_User) {
        this.ID_User = ID_User;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getMail() {
        return Mail;
    }

    public void setMail(String Mail) {
        this.Mail = Mail;
    }
    public String getFist_name() {
        return Fist_Name;
    }

    public void setFist_name(String Fist_Name) {
        this.Fist_Name = Fist_Name;
    }

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}