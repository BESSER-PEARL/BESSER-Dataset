





import java.util.List;
import java.util.ArrayList;

public class ddsm_ZookeeperCluster extends PeerToPeerPlatform {

    private int tickTime;
    private int initLimit;
    private int syncLimit;



    public ddsm_ZookeeperCluster(
        int tickTime,        int initLimit,        int syncLimit    ) {
        super(
        );
        this.tickTime = tickTime;
        this.initLimit = initLimit;
        this.syncLimit = syncLimit;
    }


    public int getTicktime() {
        return tickTime;
    }

    public void setTicktime(int tickTime) {
        this.tickTime = tickTime;
    }
    public int getInitlimit() {
        return initLimit;
    }

    public void setInitlimit(int initLimit) {
        this.initLimit = initLimit;
    }
    public int getSynclimit() {
        return syncLimit;
    }

    public void setSynclimit(int syncLimit) {
        this.syncLimit = syncLimit;
    }


}