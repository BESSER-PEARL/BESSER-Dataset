





import java.util.List;
import java.util.ArrayList;

public class cloudml_Resource extends WithProperties {

    private String startCommand;
    private String stopCommand;
    private String retrievingCommand;
    private String configurationCommand;
    private String deployingCommand;



    public cloudml_Resource(
        String startCommand,        String stopCommand,        String retrievingCommand,        String configurationCommand,        String deployingCommand    ) {
        super(
        );
        this.startCommand = startCommand;
        this.stopCommand = stopCommand;
        this.retrievingCommand = retrievingCommand;
        this.configurationCommand = configurationCommand;
        this.deployingCommand = deployingCommand;
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
    public String getRetrievingcommand() {
        return retrievingCommand;
    }

    public void setRetrievingcommand(String retrievingCommand) {
        this.retrievingCommand = retrievingCommand;
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


}