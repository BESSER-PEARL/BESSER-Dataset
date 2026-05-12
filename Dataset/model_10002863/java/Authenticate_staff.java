





import java.util.List;
import java.util.ArrayList;

public class Authenticate_staff  {

    private String UserName;
    private String Password;
    private String Authendication_Mood;



    public Authenticate_staff(
        String UserName,        String Password,        String Authendication_Mood    ) {
        this.UserName = UserName;
        this.Password = Password;
        this.Authendication_Mood = Authendication_Mood;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getAuthendication_mood() {
        return Authendication_Mood;
    }

    public void setAuthendication_mood(String Authendication_Mood) {
        this.Authendication_Mood = Authendication_Mood;
    }


}