





import java.util.List;
import java.util.ArrayList;

public class timetrack_User  {

    private String sap_password;
    private String sap_name;
    private String name;
    private String password;



    public timetrack_User(
        String sap_password,        String sap_name,        String name,        String password    ) {
        this.sap_password = sap_password;
        this.sap_name = sap_name;
        this.name = name;
        this.password = password;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}