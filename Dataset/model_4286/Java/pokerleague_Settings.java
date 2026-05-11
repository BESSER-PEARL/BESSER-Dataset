





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Settings extends Serializable {

    private String smtpUser;
    private String smtpFrom;
    private String smtpPassword;
    private String urlBase;
    private String adminPassword;
    private String smtpPort;
    private String smtpHost;
    private String defaultTimeZone;
    private int id;



    public pokerleague_Settings(
        String smtpUser,        String smtpFrom,        String smtpPassword,        String urlBase,        String adminPassword,        String smtpPort,        String smtpHost,        String defaultTimeZone,        int id    ) {
        super(
        );
        this.smtpUser = smtpUser;
        this.smtpFrom = smtpFrom;
        this.smtpPassword = smtpPassword;
        this.urlBase = urlBase;
        this.adminPassword = adminPassword;
        this.smtpPort = smtpPort;
        this.smtpHost = smtpHost;
        this.defaultTimeZone = defaultTimeZone;
        this.id = id;
    }


    public String getSmtpuser() {
        return smtpUser;
    }

    public void setSmtpuser(String smtpUser) {
        this.smtpUser = smtpUser;
    }
    public String getSmtpfrom() {
        return smtpFrom;
    }

    public void setSmtpfrom(String smtpFrom) {
        this.smtpFrom = smtpFrom;
    }
    public String getSmtppassword() {
        return smtpPassword;
    }

    public void setSmtppassword(String smtpPassword) {
        this.smtpPassword = smtpPassword;
    }
    public String getUrlbase() {
        return urlBase;
    }

    public void setUrlbase(String urlBase) {
        this.urlBase = urlBase;
    }
    public String getAdminpassword() {
        return adminPassword;
    }

    public void setAdminpassword(String adminPassword) {
        this.adminPassword = adminPassword;
    }
    public String getSmtpport() {
        return smtpPort;
    }

    public void setSmtpport(String smtpPort) {
        this.smtpPort = smtpPort;
    }
    public String getSmtphost() {
        return smtpHost;
    }

    public void setSmtphost(String smtpHost) {
        this.smtpHost = smtpHost;
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


}