





import java.util.List;
import java.util.ArrayList;

public class camel_deployment_Configuration extends DeploymentElement {

    private String stopCommand;
    private String uploadCommand;
    private String startCommand;
    private String installCommand;
    private String configureCommand;
    private String downloadCommand;



    public camel_deployment_Configuration(
        String stopCommand,        String uploadCommand,        String startCommand,        String installCommand,        String configureCommand,        String downloadCommand    ) {
        super(
        );
        this.stopCommand = stopCommand;
        this.uploadCommand = uploadCommand;
        this.startCommand = startCommand;
        this.installCommand = installCommand;
        this.configureCommand = configureCommand;
        this.downloadCommand = downloadCommand;
    }


    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
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
    public String getDownloadcommand() {
        return downloadCommand;
    }

    public void setDownloadcommand(String downloadCommand) {
        this.downloadCommand = downloadCommand;
    }


}