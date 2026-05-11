





import java.util.List;
import java.util.ArrayList;

public class db_config_TelephonySubsystem extends ServerResource {

    private boolean enabled;
    private String managerPassword;
    private String promptDirectory;
    private boolean running;
    private String managerName;
    private boolean private;
    private String visibleSafiServerIP;
    private String platformId;
    private int managerPort;
    private String hostname;
    private String versionId;



    public db_config_TelephonySubsystem(
        boolean enabled,        String managerPassword,        String promptDirectory,        boolean running,        String managerName,        boolean private,        String visibleSafiServerIP,        String platformId,        int managerPort,        String hostname,        String versionId    ) {
        super(
        );
        this.enabled = enabled;
        this.managerPassword = managerPassword;
        this.promptDirectory = promptDirectory;
        this.running = running;
        this.managerName = managerName;
        this.private = private;
        this.visibleSafiServerIP = visibleSafiServerIP;
        this.platformId = platformId;
        this.managerPort = managerPort;
        this.hostname = hostname;
        this.versionId = versionId;
    }


    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public String getManagerpassword() {
        return managerPassword;
    }

    public void setManagerpassword(String managerPassword) {
        this.managerPassword = managerPassword;
    }
    public String getPromptdirectory() {
        return promptDirectory;
    }

    public void setPromptdirectory(String promptDirectory) {
        this.promptDirectory = promptDirectory;
    }
    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }
    public String getManagername() {
        return managerName;
    }

    public void setManagername(String managerName) {
        this.managerName = managerName;
    }
    public boolean getPrivate() {
        return private;
    }

    public void setPrivate(boolean private) {
        this.private = private;
    }
    public String getVisiblesafiserverip() {
        return visibleSafiServerIP;
    }

    public void setVisiblesafiserverip(String visibleSafiServerIP) {
        this.visibleSafiServerIP = visibleSafiServerIP;
    }
    public String getPlatformid() {
        return platformId;
    }

    public void setPlatformid(String platformId) {
        this.platformId = platformId;
    }
    public int getManagerport() {
        return managerPort;
    }

    public void setManagerport(int managerPort) {
        this.managerPort = managerPort;
    }
    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }
    public String getVersionid() {
        return versionId;
    }

    public void setVersionid(String versionId) {
        this.versionId = versionId;
    }


}