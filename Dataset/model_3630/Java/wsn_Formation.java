





import java.util.List;
import java.util.ArrayList;

public class wsn_Formation  {

    private String routing;





    private wsn_Cluster wsn_cluster;




    private wsn_Activity wsn_activity;


    public wsn_Formation(
        String routing    ) {
        this.routing = routing;
    }


    public String getRouting() {
        return routing;
    }

    public void setRouting(String routing) {
        this.routing = routing;
    }

    public wsn_Cluster getWsn_cluster() {
        return wsn_cluster;
    }

    public void setWsn_cluster(wsn_Cluster wsn_cluster) {
        this.wsn_cluster = wsn_cluster;
    }
    public wsn_Activity getWsn_activity() {
        return wsn_activity;
    }

    public void setWsn_activity(wsn_Activity wsn_activity) {
        this.wsn_activity = wsn_activity;
    }

}