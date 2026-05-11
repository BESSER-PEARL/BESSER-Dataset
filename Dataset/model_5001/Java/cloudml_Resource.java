





import java.util.List;
import java.util.ArrayList;

public class cloudml_Resource extends WithProperties {

    private String stopCommand;
    private String deployingCommand;
    private String startCommand;
    private String configurationCommand;
    private String retrievingCommand;





    private cloudml_Artefact cloudml_artefact;


    public cloudml_Resource(
        String stopCommand,        String deployingCommand,        String startCommand,        String configurationCommand,        String retrievingCommand    ) {
        super(
        );
        this.stopCommand = stopCommand;
        this.deployingCommand = deployingCommand;
        this.startCommand = startCommand;
        this.configurationCommand = configurationCommand;
        this.retrievingCommand = retrievingCommand;
    }


    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }
    public String getDeployingcommand() {
        return deployingCommand;
    }

    public void setDeployingcommand(String deployingCommand) {
        this.deployingCommand = deployingCommand;
    }
    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
    }
    public String getConfigurationcommand() {
        return configurationCommand;
    }

    public void setConfigurationcommand(String configurationCommand) {
        this.configurationCommand = configurationCommand;
    }
    public String getRetrievingcommand() {
        return retrievingCommand;
    }

    public void setRetrievingcommand(String retrievingCommand) {
        this.retrievingCommand = retrievingCommand;
    }

    public cloudml_Artefact getCloudml_artefact() {
        return cloudml_artefact;
    }

    public void setCloudml_artefact(cloudml_Artefact cloudml_artefact) {
        this.cloudml_artefact = cloudml_artefact;
    }

}