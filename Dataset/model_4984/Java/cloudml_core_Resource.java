





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends CloudMLElementWithProperties {

    private boolean executeLocally;
    private String uploadCommand;
    private String startCommand;
    private String downloadCommand;
    private String stopCommand;
    private String configureCommand;
    private boolean requireCredentials;
    private String installCommand;



    public cloudml_core_Resource(
        boolean executeLocally,        String uploadCommand,        String startCommand,        String downloadCommand,        String stopCommand,        String configureCommand,        boolean requireCredentials,        String installCommand    ) {
        super(
        );
        this.executeLocally = executeLocally;
        this.uploadCommand = uploadCommand;
        this.startCommand = startCommand;
        this.downloadCommand = downloadCommand;
        this.stopCommand = stopCommand;
        this.configureCommand = configureCommand;
        this.requireCredentials = requireCredentials;
        this.installCommand = installCommand;
    }


    public boolean getExecutelocally() {
        return executeLocally;
    }

    public void setExecutelocally(boolean executeLocally) {
        this.executeLocally = executeLocally;
    }
    public String getUploadcommand() {
        return uploadCommand;
    }

    public void setUploadcommand(String uploadCommand) {
        this.uploadCommand = uploadCommand;
    }
    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
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
    public String getConfigurecommand() {
        return configureCommand;
    }

    public void setConfigurecommand(String configureCommand) {
        this.configureCommand = configureCommand;
    }
    public boolean getRequirecredentials() {
        return requireCredentials;
    }

    public void setRequirecredentials(boolean requireCredentials) {
        this.requireCredentials = requireCredentials;
    }
    public String getInstallcommand() {
        return installCommand;
    }

    public void setInstallcommand(String installCommand) {
        this.installCommand = installCommand;
    }


}