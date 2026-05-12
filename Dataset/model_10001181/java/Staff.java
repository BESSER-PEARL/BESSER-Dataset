





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Authendication_Mood;
    private String Password;
    private String UserName;



    public Staff(
        String Authendication_Mood,        String Password,        String UserName    ) {
        this.Authendication_Mood = Authendication_Mood;
        this.Password = Password;
        this.UserName = UserName;
    }


    public String getAuthendication_mood() {
        return Authendication_Mood;
    }

    public void setAuthendication_mood(String Authendication_Mood) {
        this.Authendication_Mood = Authendication_Mood;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }


}