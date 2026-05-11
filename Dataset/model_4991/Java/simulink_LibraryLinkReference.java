





import java.util.List;
import java.util.ArrayList;

public class simulink_LibraryLinkReference extends SimulinkReference {

    private boolean disabled;





    private simulink_Block simulink_block;


    public simulink_LibraryLinkReference(
        boolean disabled    ) {
        super(
        );
        this.disabled = disabled;
    }


    public boolean getDisabled() {
        return disabled;
    }

    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }

    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }

}