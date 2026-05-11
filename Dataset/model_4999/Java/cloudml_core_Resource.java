





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Resource extends WithProperties {

    private String deployingResourceCommand;
    private String retrievingResourceCommand;



    public cloudml_core_Resource(
        String deployingResourceCommand,        String retrievingResourceCommand    ) {
        super(
        );
        this.deployingResourceCommand = deployingResourceCommand;
        this.retrievingResourceCommand = retrievingResourceCommand;
    }


    public String getDeployingresourcecommand() {
        return deployingResourceCommand;
    }

    public void setDeployingresourcecommand(String deployingResourceCommand) {
        this.deployingResourceCommand = deployingResourceCommand;
    }
    public String getRetrievingresourcecommand() {
        return retrievingResourceCommand;
    }

    public void setRetrievingresourcecommand(String retrievingResourceCommand) {
        this.retrievingResourceCommand = retrievingResourceCommand;
    }


}