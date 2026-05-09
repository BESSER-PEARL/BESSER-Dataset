





import java.util.List;
import java.util.ArrayList;

public class simulink_msglib_CommunicationSwitch extends Block {

    private int debug;



    public simulink_msglib_CommunicationSwitch(
        int debug    ) {
        super(
        );
        this.debug = debug;
    }


    public int getDebug() {
        return debug;
    }

    public void setDebug(int debug) {
        this.debug = debug;
    }


}