





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends CloudMLElementWithProperties {

    private String startCommand;
    private String uploadCommand;
    private boolean requireCredentials;
    private String downloadCommand;
    private String stopCommand;
    private String installCommand;
    private String configureCommand;
    private boolean executeLocally;



    public cloudml_core_Resource(
        String startCommand,        String uploadCommand,        boolean requireCredentials,        String downloadCommand,        String stopCommand,        String installCommand,        String configureCommand,        boolean executeLocally    ) {
        super(
        );
        this.startCommand = startCommand;
        this.uploadCommand = uploadCommand;
        this.requireCredentials = requireCredentials;
        this.downloadCommand = downloadCommand;
        this.stopCommand = stopCommand;
        this.installCommand = installCommand;
        this.configureCommand = configureCommand;
        this.executeLocally = executeLocally;
    }


    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
    }
    public String getUploadcommand() {
        return uploadCommand;
    }

    public void setUploadcommand(String uploadCommand) {
        this.uploadCommand = uploadCommand;
    }
    public boolean getRequirecredentials() {
        return requireCredentials;
    }

    public void setRequirecredentials(boolean requireCredentials) {
        this.requireCredentials = requireCredentials;
    }
    public String getDownloadcommand() {
        return downloadCommand;
    }

    public void setDownloadcommand(String downloadCommand) {
        this.downloadCommand = downloadCommand;
    }
    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }
    public String getInstallcommand() {
        return installCommand;
    }

    public void setInstallcommand(String installCommand) {
        this.installCommand = installCommand;
    }
    public String getConfigurecommand() {
        return configureCommand;
    }

    public void setConfigurecommand(String configureCommand) {
        this.configureCommand = configureCommand;
    }
    public boolean getExecutelocally() {
        return executeLocally;
    }

    public void setExecutelocally(boolean executeLocally) {
        this.executeLocally = executeLocally;
    }


}