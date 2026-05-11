





import java.util.List;
import java.util.ArrayList;

public class simulink_SubSystem extends Block {

    private String tag;





    private simulink_Block simulink_block;




    private List<simulink_Block> simulink_blocks;


    public simulink_SubSystem(
        String tag    ) {
        super(
        );
        this.tag = tag;
        this.simulink_blocks = new ArrayList<>();
    }

    public simulink_SubSystem(
        String tag        ArrayList<simulink_Block> simulink_blocks    ) {
        this.tag = tag;
        this.simulink_blocks = simulink_blocks;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
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

}