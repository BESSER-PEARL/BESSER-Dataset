





import java.util.List;
import java.util.ArrayList;

public class Origination  {

    private String Logo;
    private String Executive_manager;
    private String Full_name;
    private String General_supervisor;





    private Admin admin;


    public Origination(
        String Logo,        String Executive_manager,        String Full_name,        String General_supervisor    ) {
        this.Logo = Logo;
        this.Executive_manager = Executive_manager;
        this.Full_name = Full_name;
        this.General_supervisor = General_supervisor;
    }


    public String getLogo() {
        return Logo;
    }

    public void setLogo(String Logo) {
        this.Logo = Logo;
    }
    public String getExecutive_manager() {
        return Executive_manager;
    }

    public void setExecutive_manager(String Executive_manager) {
        this.Executive_manager = Executive_manager;
    }
    public String getFull_name() {
        return Full_name;
    }

    public void setFull_name(String Full_name) {
        this.Full_name = Full_name;
    }
    public String getGeneral_supervisor() {
        return General_supervisor;
    }

    public void setGeneral_supervisor(String General_supervisor) {
        this.General_supervisor = General_supervisor;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}