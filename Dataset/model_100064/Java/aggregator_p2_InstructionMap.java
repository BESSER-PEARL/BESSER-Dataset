





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_InstructionMap  {

    private String key;





    private TouchpointInstruction touchpointinstruction;


    public aggregator_p2_InstructionMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public TouchpointInstruction getTouchpointinstruction() {
        return touchpointinstruction;
    }

    public void setTouchpointinstruction(TouchpointInstruction touchpointinstruction) {
        this.touchpointinstruction = touchpointinstruction;
    }

}