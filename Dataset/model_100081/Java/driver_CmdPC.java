





import java.util.List;
import java.util.ArrayList;

public class driver_CmdPC  {

    private String sync;
    private String uRI;
    private String value;
    private String phase;



    public driver_CmdPC(
        String sync,        String uRI,        String value,        String phase    ) {
        this.sync = sync;
        this.uRI = uRI;
        this.value = value;
        this.phase = phase;
    }


    public String getSync() {
        return sync;
    }

    public void setSync(String sync) {
        this.sync = sync;
    }
    public String getUri() {
        return uRI;
    }

    public void setUri(String uRI) {
        this.uRI = uRI;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getPhase() {
        return phase;
    }

    public void setPhase(String phase) {
        this.phase = phase;
    }


}