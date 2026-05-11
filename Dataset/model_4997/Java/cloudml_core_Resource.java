





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends WithProperties {

    private String startCommand;
    private String deployingCommand;
    private String retrievingCommand;
    private String configurationCommand;



    public cloudml_core_Resource(
        String startCommand,        String deployingCommand,        String retrievingCommand,        String configurationCommand    ) {
        super(
        );
        this.startCommand = startCommand;
        this.deployingCommand = deployingCommand;
        this.retrievingCommand = retrievingCommand;
        this.configurationCommand = configurationCommand;
    }


    public String getStartcommand() {
        return startCommand;
    }

    public void setStartcommand(String startCommand) {
        this.startCommand = startCommand;
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
    public String getConfigurationcommand() {
        return configurationCommand;
    }

    public void setConfigurationcommand(String configurationCommand) {
        this.configurationCommand = configurationCommand;
    }


}