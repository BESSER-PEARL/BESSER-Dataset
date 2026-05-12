





import java.util.List;
import java.util.ArrayList;

public class db_config_TelephonySubsystem extends ServerResource {

    private String managerName;
    private String promptDirectory;
    private String managerPassword;
    private boolean running;
    private int managerPort;
    private String platformId;
    private String visibleSafiServerIP;
    private String versionId;
    private boolean enabled;
    private boolean private;
    private String hostname;



    public db_config_TelephonySubsystem(
        String managerName,        String promptDirectory,        String managerPassword,        boolean running,        int managerPort,        String platformId,        String visibleSafiServerIP,        String versionId,        boolean enabled,        boolean private,        String hostname    ) {
        super(
        );
        this.managerName = managerName;
        this.promptDirectory = promptDirectory;
        this.managerPassword = managerPassword;
        this.running = running;
        this.managerPort = managerPort;
        this.platformId = platformId;
        this.visibleSafiServerIP = visibleSafiServerIP;
        this.versionId = versionId;
        this.enabled = enabled;
        this.private = private;
        this.hostname = hostname;
    }


    public String getManagername() {
        return managerName;
    }

    public void setManagername(String managerName) {
        this.managerName = managerName;
    }
    public String getPromptdirectory() {
        return promptDirectory;
    }

    public void setPromptdirectory(String promptDirectory) {
        this.promptDirectory = promptDirectory;
    }
    public String getManagerpassword() {
        return managerPassword;
    }

    public void setManagerpassword(String managerPassword) {
        this.managerPassword = managerPassword;
    }
    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }
    public int getManagerport() {
        return managerPort;
    }

    public void setManagerport(int managerPort) {
        this.managerPort = managerPort;
    }
    public String getPlatformid() {
        return platformId;
    }

    public void setPlatformid(String platformId) {
        this.platformId = platformId;
    }
    public String getVisiblesafiserverip() {
        return visibleSafiServerIP;
    }

    public void setVisiblesafiserverip(String visibleSafiServerIP) {
        this.visibleSafiServerIP = visibleSafiServerIP;
    }
    public String getVersionid() {
        return versionId;
    }

    public void setVersionid(String versionId) {
        this.versionId = versionId;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public boolean getPrivate() {
        return private;
    }

    public void setPrivate(boolean private) {
        this.private = private;
    }
    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }


}