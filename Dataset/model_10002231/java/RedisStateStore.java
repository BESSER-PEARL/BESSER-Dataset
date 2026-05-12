





import java.util.List;
import java.util.ArrayList;

public class RedisStateStore  {

    private String log;
    private None cluster;
    private None RadixClient;



    public RedisStateStore(
        String log,        None cluster,        None RadixClient    ) {
        this.log = log;
        this.cluster = cluster;
        this.RadixClient = RadixClient;
    }


    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
    }
    public None getCluster() {
        return cluster;
    }

    public void setCluster(None cluster) {
        this.cluster = cluster;
    }
    public None getRadixclient() {
        return RadixClient;
    }

    public void setRadixclient(None RadixClient) {
        this.RadixClient = RadixClient;
    }


}