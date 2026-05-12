





import java.util.List;
import java.util.ArrayList;

public class dataflownet_Process extends NamedElement {

    private String host;





    private dataflownet_DataflowSystem dataflownet_dataflowsystem;


    public dataflownet_Process(
        String host    ) {
        super(
        );
        this.host = host;
    }


    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public dataflownet_DataflowSystem getDataflownet_dataflowsystem() {
        return dataflownet_dataflowsystem;
    }

    public void setDataflownet_dataflowsystem(dataflownet_DataflowSystem dataflownet_dataflowsystem) {
        this.dataflownet_dataflowsystem = dataflownet_dataflowsystem;
    }

}