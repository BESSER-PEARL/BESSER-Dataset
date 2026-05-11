





import java.util.List;
import java.util.ArrayList;

public class cloudml_Resource extends CloudMLElementWithProperties {

    private String installCommand;
    private String configureCommand;
    private String startCommand;
    private boolean requireCredentials;
    private String downloadCommand;
    private String uploadCommand;
    private boolean executeLocally;
    private String stopCommand;



    public cloudml_Resource(
        String installCommand,        String configureCommand,        String startCommand,        boolean requireCredentials,        String downloadCommand,        String uploadCommand,        boolean executeLocally,        String stopCommand    ) {
        super(
        );
        this.installCommand = installCommand;
        this.configureCommand = configureCommand;
        this.startCommand = startCommand;
        this.requireCredentials = requireCredentials;
        this.downloadCommand = downloadCommand;
        this.uploadCommand = uploadCommand;
        this.executeLocally = executeLocally;
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
    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
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
    public String getUploadcommand() {
        return uploadCommand;
    }

    public void setUploadcommand(String uploadCommand) {
        this.uploadCommand = uploadCommand;
    }
    public boolean getExecutelocally() {
        return executeLocally;
    }

    public void setExecutelocally(boolean executeLocally) {
        this.executeLocally = executeLocally;
    }
    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }


}