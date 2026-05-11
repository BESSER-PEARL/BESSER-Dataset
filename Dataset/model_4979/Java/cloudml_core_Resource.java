





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends CloudMLElementWithProperties {

    private boolean executeLocally;
    private String installCommand;
    private String downloadCommand;
    private String configureCommand;
    private String uploadCommand;
    private boolean requireCredentials;
    private String stopCommand;
    private String startCommand;



    public cloudml_core_Resource(
        boolean executeLocally,        String installCommand,        String downloadCommand,        String configureCommand,        String uploadCommand,        boolean requireCredentials,        String stopCommand,        String startCommand    ) {
        super(
        );
        this.executeLocally = executeLocally;
        this.installCommand = installCommand;
        this.downloadCommand = downloadCommand;
        this.configureCommand = configureCommand;
        this.uploadCommand = uploadCommand;
        this.requireCredentials = requireCredentials;
        this.stopCommand = stopCommand;
        this.startCommand = startCommand;
    }


    public boolean getExecutelocally() {
        return executeLocally;
    }

    public void setExecutelocally(boolean executeLocally) {
        this.executeLocally = executeLocally;
    }
    public String getInstallcommand() {
        return installCommand;
    }

    public void setInstallcommand(String installCommand) {
        this.installCommand = installCommand;
    }
    public String getDownloadcommand() {
        return downloadCommand;
    }

    public void setDownloadcommand(String downloadCommand) {
        this.downloadCommand = downloadCommand;
    }
    public String getConfigurecommand() {
        return configureCommand;
    }

    public void setConfigurecommand(String configureCommand) {
        this.configureCommand = configureCommand;
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
    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }
    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
    }


}