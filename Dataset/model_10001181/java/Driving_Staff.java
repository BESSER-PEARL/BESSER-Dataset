





import java.util.List;
import java.util.ArrayList;

public class Driving_Staff  {

    private String Pilot_ContactNo;
    private String Password;
    private String PilotName;
    private String Authendication_Mood;





    private Staff staff;


    public Driving_Staff(
        String Pilot_ContactNo,        String Password,        String PilotName,        String Authendication_Mood    ) {
        this.Pilot_ContactNo = Pilot_ContactNo;
        this.Password = Password;
        this.PilotName = PilotName;
        this.Authendication_Mood = Authendication_Mood;
    }


    public String getPilot_contactno() {
        return Pilot_ContactNo;
    }

    public void setPilot_contactno(String Pilot_ContactNo) {
        this.Pilot_ContactNo = Pilot_ContactNo;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getPilotname() {
        return PilotName;
    }

    public void setPilotname(String PilotName) {
        this.PilotName = PilotName;
    }
    public String getAuthendication_mood() {
        return Authendication_Mood;
    }

    public void setAuthendication_mood(String Authendication_Mood) {
        this.Authendication_Mood = Authendication_Mood;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}