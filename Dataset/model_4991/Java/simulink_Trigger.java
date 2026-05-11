





import java.util.List;
import java.util.ArrayList;

public class simulink_Trigger extends InPort {

    private String statesWhenEnabling;
    private String triggerType;





    private simulink_Block simulink_block;


    public simulink_Trigger(
        String statesWhenEnabling,        String triggerType    ) {
        super(
        );
        this.statesWhenEnabling = statesWhenEnabling;
        this.triggerType = triggerType;
    }


    public String getStateswhenenabling() {
        return statesWhenEnabling;
    }

    public void setStateswhenenabling(String statesWhenEnabling) {
        this.statesWhenEnabling = statesWhenEnabling;
    }
    public String getTriggertype() {
        return triggerType;
    }

    public void setTriggertype(String triggerType) {
        this.triggerType = triggerType;
    }

    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }

}