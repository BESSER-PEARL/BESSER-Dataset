





import java.util.List;
import java.util.ArrayList;

public class RedisStateStore  {

    private None cluster;
    private None RadixClient;
    private String log;



    public RedisStateStore(
        None cluster,        None RadixClient,        String log    ) {
        this.cluster = cluster;
        this.RadixClient = RadixClient;
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
    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
    }


}