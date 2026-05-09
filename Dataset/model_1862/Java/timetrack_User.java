





import java.util.List;
import java.util.ArrayList;

public class timetrack_User  {

    private String password;
    private String name;
    private String sap_password;
    private String sap_name;





    private timetrack_Library timetrack_library;


    public timetrack_User(
        String password,        String name,        String sap_password,        String sap_name    ) {
        this.password = password;
        this.name = name;
        this.sap_password = sap_password;
        this.sap_name = sap_name;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSap_password() {
        return sap_password;
    }

    public void setSap_password(String sap_password) {
        this.sap_password = sap_password;
    }
    public String getSap_name() {
        return sap_name;
    }

    public void setSap_name(String sap_name) {
        this.sap_name = sap_name;
    }

    public timetrack_Library getTimetrack_library() {
        return timetrack_library;
    }

    public void setTimetrack_library(timetrack_Library timetrack_library) {
        this.timetrack_library = timetrack_library;
    }

}