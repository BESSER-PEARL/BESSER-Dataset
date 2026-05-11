





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Settings extends Serializable {

    private String defaultTimeZone;
    private int id;
    private String adminPassword;



    public pokerleague_Settings(
        String defaultTimeZone,        int id,        String adminPassword    ) {
        super(
        );
        this.defaultTimeZone = defaultTimeZone;
        this.id = id;
        this.adminPassword = adminPassword;
    }


    public String getDefaulttimezone() {
        return defaultTimeZone;
    }

    public void setDefaulttimezone(String defaultTimeZone) {
        this.defaultTimeZone = defaultTimeZone;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAdminpassword() {
        return adminPassword;
    }

    public void setAdminpassword(String adminPassword) {
        this.adminPassword = adminPassword;
    }


}