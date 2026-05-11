





import java.util.List;
import java.util.ArrayList;

public class co2_TellAndWait extends Process {

    private boolean timeout;



    public co2_TellAndWait(
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


}