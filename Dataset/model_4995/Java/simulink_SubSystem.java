





import java.util.List;
import java.util.ArrayList;

public class simulink_SubSystem extends Block {






    private simulink_Block simulink_block;




    private List<simulink_Block> simulink_blocks;




    private List<simulink_Connection> simulink_connections;


    public simulink_SubSystem(
    ) {
        super(
        );
        this.simulink_blocks = new ArrayList<>();
        this.simulink_connections = new ArrayList<>();
    }

    public simulink_SubSystem(
        ArrayList<simulink_Block> simulink_blocks,        ArrayList<simulink_Connection> simulink_connections    ) {
        this.simulink_blocks = simulink_blocks;
        this.simulink_connections = simulink_connections;
    }


    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }
    public List<simulink_Block> getSimulink_blocks() {
        return simulink_blocks;
    }

    public void addSimulink_block(Simulink_block simulink_block) {
        this.simulink_blocks.add(simulink_block);
    }
    public List<simulink_Connection> getSimulink_connections() {
        return simulink_connections;
    }

    public void addSimulink_connection(Simulink_connection simulink_connection) {
        this.simulink_connections.add(simulink_connection);
    }

}