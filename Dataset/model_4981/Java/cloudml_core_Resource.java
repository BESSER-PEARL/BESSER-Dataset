





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends CloudMLElementWithProperties {

    private String stopCommand;
    private boolean requireCredentials;
    private String startCommand;
    private String uploadCommand;
    private String downloadCommand;
    private boolean executeLocally;
    private String installCommand;
    private String configureCommand;



    public cloudml_core_Resource(
        String stopCommand,        boolean requireCredentials,        String startCommand,        String uploadCommand,        String downloadCommand,        boolean executeLocally,        String installCommand,        String configureCommand    ) {
        super(
        );
        this.stopCommand = stopCommand;
        this.requireCredentials = requireCredentials;
        this.startCommand = startCommand;
        this.uploadCommand = uploadCommand;
        this.downloadCommand = downloadCommand;
        this.executeLocally = executeLocally;
        this.installCommand = installCommand;
        this.configureCommand = configureCommand;
    }


    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }
    public boolean getRequirecredentials() {
        return requireCredentials;
    }

    public void setRequirecredentials(boolean requireCredentials) {
        this.requireCredentials = requireCredentials;
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
    public String getDownloadcommand() {
        return downloadCommand;
    }

    public void setDownloadcommand(String downloadCommand) {
        this.downloadCommand = downloadCommand;
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
    public String getConfigurecommand() {
        return configureCommand;
    }

    public void setConfigurecommand(String configureCommand) {
        this.configureCommand = configureCommand;
    }


}