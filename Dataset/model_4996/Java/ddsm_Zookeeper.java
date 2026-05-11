





import java.util.List;
import java.util.ArrayList;

public class ddsm_Zookeeper extends InternalComponent {

    private String initLimit;
    private String syncLimit;
    private String tickTime;



    public ddsm_Zookeeper(
        String initLimit,        String syncLimit,        String tickTime    ) {
        super(
        );
        this.initLimit = initLimit;
        this.syncLimit = syncLimit;
        this.tickTime = tickTime;
    }


    public String getInitlimit() {
        return initLimit;
    }

    public void setInitlimit(String initLimit) {
        this.initLimit = initLimit;
    }
    public String getSynclimit() {
        return syncLimit;
    }

    public void setSynclimit(String syncLimit) {
        this.syncLimit = syncLimit;
    }
    public String getTicktime() {
        return tickTime;
    }

    public void setTicktime(String tickTime) {
        this.tickTime = tickTime;
    }


}