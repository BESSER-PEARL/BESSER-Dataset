





import java.util.List;
import java.util.ArrayList;

public class co2_Receive extends ReceiveGroup {

    private boolean timeout;





    private co2_TimeoutProcess co2_timeoutprocess;


    public co2_Receive(
        boolean timeout    ) {
        super(
        );
        this.timeout = timeout;
    }


    public boolean getTimeout() {
        return timeout;
    }

    public void setTimeout(boolean timeout) {
        this.timeout = timeout;
    }

    public co2_TimeoutProcess getCo2_timeoutprocess() {
        return co2_timeoutprocess;
    }

    public void setCo2_timeoutprocess(co2_TimeoutProcess co2_timeoutprocess) {
        this.co2_timeoutprocess = co2_timeoutprocess;
    }

}