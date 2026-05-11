





import java.util.List;
import java.util.ArrayList;

public class cloudml_Resource extends CloudMLElementWithProperties {

    private String startCommand;
    private String uploadCommand;
    private String installCommand;
    private boolean executeLocally;
    private String stopCommand;
    private String configureCommand;
    private String downloadCommand;
    private boolean requireCredentials;



    public cloudml_Resource(
        String startCommand,        String uploadCommand,        String installCommand,        boolean executeLocally,        String stopCommand,        String configureCommand,        String downloadCommand,        boolean requireCredentials    ) {
        super(
        );
        this.startCommand = startCommand;
        this.uploadCommand = uploadCommand;
        this.installCommand = installCommand;
        this.executeLocally = executeLocally;
        this.stopCommand = stopCommand;
        this.configureCommand = configureCommand;
        this.downloadCommand = downloadCommand;
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
    public String getInstallcommand() {
        return installCommand;
    }

    public void setInstallcommand(String installCommand) {
        this.installCommand = installCommand;
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
    public String getConfigurecommand() {
        return configureCommand;
    }

    public void setConfigurecommand(String configureCommand) {
        this.configureCommand = configureCommand;
    }
    public String getDownloadcommand() {
        return downloadCommand;
    }

    public void setDownloadcommand(String downloadCommand) {
        this.downloadCommand = downloadCommand;
    }
    public boolean getRequirecredentials() {
        return requireCredentials;
    }

    public void setRequirecredentials(boolean requireCredentials) {
        this.requireCredentials = requireCredentials;
    }


}