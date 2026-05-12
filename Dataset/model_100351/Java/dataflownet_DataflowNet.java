





import java.util.List;
import java.util.ArrayList;

public class dataflownet_DataflowNet extends Node {






    private List<dataflownet_Channel> dataflownet_channels;




    private dataflownet_Node dataflownet_node;




    private List<dataflownet_Node> dataflownet_nodes;




    private dataflownet_DataflowSystem dataflownet_dataflowsystem;




    private List<dataflownet_Channel> dataflownet_channels;




    private List<dataflownet_Channel> dataflownet_channels;




    private dataflownet_Process dataflownet_process;


    public dataflownet_DataflowNet(
    ) {
        super(
        );
        this.dataflownet_channels = new ArrayList<>();
        this.dataflownet_nodes = new ArrayList<>();
        this.dataflownet_channels = new ArrayList<>();
        this.dataflownet_channels = new ArrayList<>();
    }

    public dataflownet_DataflowNet(
        ArrayList<dataflownet_Channel> dataflownet_channels,        ArrayList<dataflownet_Node> dataflownet_nodes,        ArrayList<dataflownet_Channel> dataflownet_channels,        ArrayList<dataflownet_Channel> dataflownet_channels    ) {
        this.dataflownet_channels = dataflownet_channels;
        this.dataflownet_nodes = dataflownet_nodes;
        this.dataflownet_channels = dataflownet_channels;
        this.dataflownet_channels = dataflownet_channels;
    }


    public List<dataflownet_Channel> getDataflownet_channels() {
        return dataflownet_channels;
    }

    public void addDataflownet_channel(Dataflownet_channel dataflownet_channel) {
        this.dataflownet_channels.add(dataflownet_channel);
    }
    public dataflownet_Node getDataflownet_node() {
        return dataflownet_node;
    }

    public void setDataflownet_node(dataflownet_Node dataflownet_node) {
        this.dataflownet_node = dataflownet_node;
    }
    public List<dataflownet_Node> getDataflownet_nodes() {
        return dataflownet_nodes;
    }

    public void addDataflownet_node(Dataflownet_node dataflownet_node) {
        this.dataflownet_nodes.add(dataflownet_node);
    }
    public dataflownet_DataflowSystem getDataflownet_dataflowsystem() {
        return dataflownet_dataflowsystem;
    }

    public void setDataflownet_dataflowsystem(dataflownet_DataflowSystem dataflownet_dataflowsystem) {
        this.dataflownet_dataflowsystem = dataflownet_dataflowsystem;
    }
    public List<dataflownet_Channel> getDataflownet_channels() {
        return dataflownet_channels;
    }

    public void addDataflownet_channel(Dataflownet_channel dataflownet_channel) {
        this.dataflownet_channels.add(dataflownet_channel);
    }
    public List<dataflownet_Channel> getDataflownet_channels() {
        return dataflownet_channels;
    }

    public void addDataflownet_channel(Dataflownet_channel dataflownet_channel) {
        this.dataflownet_channels.add(dataflownet_channel);
    }
    public dataflownet_Process getDataflownet_process() {
        return dataflownet_process;
    }

    public void setDataflownet_process(dataflownet_Process dataflownet_process) {
        this.dataflownet_process = dataflownet_process;
    }

}