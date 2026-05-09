





import java.util.List;
import java.util.ArrayList;

public class rtsc_Transition extends NamedElement {

    private int hitCount;





    private rtsc_State rtsc_state;




    private List<rtsc_MessageType> rtsc_messagetypes;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_State rtsc_state;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_State rtsc_state;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_State rtsc_state;


    public rtsc_Transition(
        int hitCount    ) {
        super(
        );
        this.hitCount = hitCount;
        this.rtsc_messagetypes = new ArrayList<>();
    }

    public rtsc_Transition(
        int hitCount        ArrayList<rtsc_MessageType> rtsc_messagetypes    ) {
        this.hitCount = hitCount;
        this.rtsc_messagetypes = rtsc_messagetypes;
    }

    public int getHitcount() {
        return hitCount;
    }

    public void setHitcount(int hitCount) {
        this.hitCount = hitCount;
    }

    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }
    public List<rtsc_MessageType> getRtsc_messagetypes() {
        return rtsc_messagetypes;
    }

    public void addRtsc_messagetype(Rtsc_messagetype rtsc_messagetype) {
        this.rtsc_messagetypes.add(rtsc_messagetype);
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_State getRtsc_state() {
        return rtsc_state;
    }

    public void setRtsc_state(rtsc_State rtsc_state) {
        this.rtsc_state = rtsc_state;
    }

}