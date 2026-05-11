





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends WithProperties {

    private String startCommand;
    private String configurationCommand;
    private String retrievingCommand;
    private String deployingCommand;



    public cloudml_core_Resource(
        String startCommand,        String configurationCommand,        String retrievingCommand,        String deployingCommand    ) {
        super(
        );
        this.startCommand = startCommand;
        this.configurationCommand = configurationCommand;
        this.retrievingCommand = retrievingCommand;
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
    public String getDeployingcommand() {
        return deployingCommand;
    }

    public void setDeployingcommand(String deployingCommand) {
        this.deployingCommand = deployingCommand;
    }


}