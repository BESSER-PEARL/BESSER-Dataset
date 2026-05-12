





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_Touchpoints  {






    private List<p2view_aggregator_ITouchpointData> p2view_aggregator_itouchpointdatas;


    public aggregator_p2view_Touchpoints(
    ) {
        this.p2view_aggregator_itouchpointdatas = new ArrayList<>();
    }

    public aggregator_p2view_Touchpoints(
        ArrayList<p2view_aggregator_ITouchpointData> p2view_aggregator_itouchpointdatas    ) {
        this.p2view_aggregator_itouchpointdatas = p2view_aggregator_itouchpointdatas;
    }


    public List<p2view_aggregator_ITouchpointData> getP2view_aggregator_itouchpointdatas() {
        return p2view_aggregator_itouchpointdatas;
    }

    public void addP2view_aggregator_itouchpointdata(P2view_aggregator_itouchpointdata p2view_aggregator_itouchpointdata) {
        this.p2view_aggregator_itouchpointdatas.add(p2view_aggregator_itouchpointdata);
    }

}