





import java.util.List;
import java.util.ArrayList;

public class Tuning_Staff  {

    private String Authendication_Mood;
    private String UserName;
    private String Address;





    private Staff staff;


    public Tuning_Staff(
        String Authendication_Mood,        String UserName,        String Address    ) {
        this.Authendication_Mood = Authendication_Mood;
        this.UserName = UserName;
        this.Address = Address;
    }


    public String getAuthendication_mood() {
        return Authendication_Mood;
    }

    public void setAuthendication_mood(String Authendication_Mood) {
        this.Authendication_Mood = Authendication_Mood;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}