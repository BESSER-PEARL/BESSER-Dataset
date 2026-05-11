





import java.util.List;
import java.util.ArrayList;

public class simulink_InPort extends Port {






    private simulink_Block simulink_block;


    public simulink_InPort(
    ) {
        super(
        );
    }



    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }

}