





import java.util.List;
import java.util.ArrayList;

public class simulink_Enable extends InPort {

    private String statesWhenEnabling;





    private simulink_Block simulink_block;


    public simulink_Enable(
        String statesWhenEnabling    ) {
        super(
        );
        this.statesWhenEnabling = statesWhenEnabling;
    }


    public String getStateswhenenabling() {
        return statesWhenEnabling;
    }

    public void setStateswhenenabling(String statesWhenEnabling) {
        this.statesWhenEnabling = statesWhenEnabling;
    }

    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }

}