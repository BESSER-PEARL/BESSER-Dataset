





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Analog extends Brick {

    private boolean debug;



    public arduinoML_Analog(
        boolean debug    ) {
        super(
        );
        this.debug = debug;
    }


    public boolean getDebug() {
        return debug;
    }

    public void setDebug(boolean debug) {
        this.debug = debug;
    }


}