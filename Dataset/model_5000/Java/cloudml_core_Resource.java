





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends WithProperties {

    private String configurationCommand;
    private String deployingCommand;
    private String retrievingCommand;
    private String startCommand;
    private String stopCommand;



    public cloudml_core_Resource(
        String configurationCommand,        String deployingCommand,        String retrievingCommand,        String startCommand,        String stopCommand    ) {
        super(
        );
        this.configurationCommand = configurationCommand;
        this.deployingCommand = deployingCommand;
        this.retrievingCommand = retrievingCommand;
        this.startCommand = startCommand;
        this.stopCommand = stopCommand;
    }


    public String getConfigurationcommand() {
        return configurationCommand;
    }

    public void setConfigurationcommand(String configurationCommand) {
        this.configurationCommand = configurationCommand;
    }
    public String getDeployingcommand() {
        return deployingCommand;
    }

    public void setDeployingcommand(String deployingCommand) {
        this.deployingCommand = deployingCommand;
    }
    public String getRetrievingcommand() {
        return retrievingCommand;
    }

    public void setRetrievingcommand(String retrievingCommand) {
        this.retrievingCommand = retrievingCommand;
    }
    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
    }
    public String getStopcommand() {
        return stopCommand;
    }

    public void setStopcommand(String stopCommand) {
        this.stopCommand = stopCommand;
    }


}