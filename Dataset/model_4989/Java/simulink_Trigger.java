





import java.util.List;
import java.util.ArrayList;

public class simulink_Trigger extends InPort {

    private String triggerType;
    private String statesWhenEnabling;





    private simulink_Block simulink_block;


    public simulink_Trigger(
        String triggerType,        String statesWhenEnabling    ) {
        super(
        );
        this.triggerType = triggerType;
        this.statesWhenEnabling = statesWhenEnabling;
    }


    public String getTriggertype() {
        return triggerType;
    }

    public void setTriggertype(String triggerType) {
        this.triggerType = triggerType;
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