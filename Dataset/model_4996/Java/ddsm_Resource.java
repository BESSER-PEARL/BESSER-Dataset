





import java.util.List;
import java.util.ArrayList;

public class ddsm_Resource  {

    private String resourceId;
    private String stopCommand;
    private String createCommand;
    private String configureCommand;
    private String installCommand;
    private String downloadCommand;
    private String startCommand;





    private ddsm_CloudElement ddsm_cloudelement;


    public ddsm_Resource(
        String resourceId,        String stopCommand,        String createCommand,        String configureCommand,        String installCommand,        String downloadCommand,        String startCommand    ) {
        this.resourceId = resourceId;
        this.stopCommand = stopCommand;
        this.createCommand = createCommand;
        this.configureCommand = configureCommand;
        this.installCommand = installCommand;
        this.downloadCommand = downloadCommand;
        this.startCommand = startCommand;
    }


    public String getResourceid() {
        return resourceId;
    }

    public void setResourceid(String resourceId) {
        this.resourceId = resourceId;
    }
    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }
    public String getCreatecommand() {
        return createCommand;
    }

    public void setCreatecommand(String createCommand) {
        this.createCommand = createCommand;
    }
    public String getConfigurecommand() {
        return configureCommand;
    }

    public void setConfigurecommand(String configureCommand) {
        this.configureCommand = configureCommand;
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
    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
    }

    public ddsm_CloudElement getDdsm_cloudelement() {
        return ddsm_cloudelement;
    }

    public void setDdsm_cloudelement(ddsm_CloudElement ddsm_cloudelement) {
        this.ddsm_cloudelement = ddsm_cloudelement;
    }

}