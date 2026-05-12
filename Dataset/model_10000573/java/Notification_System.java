





import java.util.List;
import java.util.ArrayList;

public class Notification_System  {

    private int PublicSafetyPage;
    private String OwnerEmail;
    private String OwnerNum__Integer;
    private int PublicSafetyNumber;





    private control_panel control_panel;


    public Notification_System(
        int PublicSafetyPage,        String OwnerEmail,        String OwnerNum__Integer,        int PublicSafetyNumber    ) {
        this.PublicSafetyPage = PublicSafetyPage;
        this.OwnerEmail = OwnerEmail;
        this.OwnerNum__Integer = OwnerNum__Integer;
        this.PublicSafetyNumber = PublicSafetyNumber;
    }


    public int getPublicsafetypage() {
        return PublicSafetyPage;
    }

    public void setPublicsafetypage(int PublicSafetyPage) {
        this.PublicSafetyPage = PublicSafetyPage;
    }
    public String getOwneremail() {
        return OwnerEmail;
    }

    public void setOwneremail(String OwnerEmail) {
        this.OwnerEmail = OwnerEmail;
    }
    public String getOwnernum__integer() {
        return OwnerNum__Integer;
    }

    public void setOwnernum__integer(String OwnerNum__Integer) {
        this.OwnerNum__Integer = OwnerNum__Integer;
    }
    public int getPublicsafetynumber() {
        return PublicSafetyNumber;
    }

    public void setPublicsafetynumber(int PublicSafetyNumber) {
        this.PublicSafetyNumber = PublicSafetyNumber;
    }

    public control_panel getControl_panel() {
        return control_panel;
    }

    public void setControl_panel(control_panel control_panel) {
        this.control_panel = control_panel;
    }

}