





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Settings extends Serializable {

    private int id;
    private String defaultTimeZone;
    private String adminPassword;



    public pokerleague_Settings(
        int id,        String defaultTimeZone,        String adminPassword    ) {
        super(
        );
        this.id = id;
        this.defaultTimeZone = defaultTimeZone;
        this.adminPassword = adminPassword;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDefaulttimezone() {
        return defaultTimeZone;
    }

    public void setDefaulttimezone(String defaultTimeZone) {
        this.defaultTimeZone = defaultTimeZone;
    }
    public String getAdminpassword() {
        return adminPassword;
    }

    public void setAdminpassword(String adminPassword) {
        this.adminPassword = adminPassword;
    }


}