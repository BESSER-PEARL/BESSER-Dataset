





import java.util.List;
import java.util.ArrayList;

public class dataflownet_DataflowSystem extends NamedElement {

    private String protocol;





    private List<dataflownet_Process> dataflownet_processs;




    private List<dataflownet_Channel> dataflownet_channels;


    public dataflownet_DataflowSystem(
        String protocol    ) {
        super(
        );
        this.protocol = protocol;
        this.dataflownet_processs = new ArrayList<>();
        this.dataflownet_channels = new ArrayList<>();
    }

    public dataflownet_DataflowSystem(
        String protocol        ArrayList<dataflownet_Process> dataflownet_processs,        ArrayList<dataflownet_Channel> dataflownet_channels    ) {
        this.protocol = protocol;
        this.dataflownet_processs = dataflownet_processs;
        this.dataflownet_channels = dataflownet_channels;
    }

    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }

    public List<dataflownet_Process> getDataflownet_processs() {
        return dataflownet_processs;
    }

    public void addDataflownet_process(Dataflownet_process dataflownet_process) {
        this.dataflownet_processs.add(dataflownet_process);
    }
    public List<dataflownet_Channel> getDataflownet_channels() {
        return dataflownet_channels;
    }

    public void addDataflownet_channel(Dataflownet_channel dataflownet_channel) {
        this.dataflownet_channels.add(dataflownet_channel);
    }

}