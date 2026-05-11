





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_Touchpoints  {






    private ITouchpointType itouchpointtype;




    private List<TouchpointData> touchpointdatas;


    public aggregator_p2view_Touchpoints(
    ) {
        this.touchpointdatas = new ArrayList<>();
    }

    public aggregator_p2view_Touchpoints(
        ArrayList<TouchpointData> touchpointdatas    ) {
        this.touchpointdatas = touchpointdatas;
    }


    public ITouchpointType getItouchpointtype() {
        return itouchpointtype;
    }

    public void setItouchpointtype(ITouchpointType itouchpointtype) {
        this.itouchpointtype = itouchpointtype;
    }
    public List<TouchpointData> getTouchpointdatas() {
        return touchpointdatas;
    }

    public void addTouchpointdata(Touchpointdata touchpointdata) {
        this.touchpointdatas.add(touchpointdata);
    }

}