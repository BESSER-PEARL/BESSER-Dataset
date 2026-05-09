





import java.util.List;
import java.util.ArrayList;

public class rtsc_MessageBuffer  {






    private rtsc_Port rtsc_port;




    private rtsc_Port rtsc_port;




    private List<rtsc_MessageType> rtsc_messagetypes;


    public rtsc_MessageBuffer(
    ) {
        this.rtsc_messagetypes = new ArrayList<>();
    }

    public rtsc_MessageBuffer(
        ArrayList<rtsc_MessageType> rtsc_messagetypes    ) {
        this.rtsc_messagetypes = rtsc_messagetypes;
    }


    public rtsc_Port getRtsc_port() {
        return rtsc_port;
    }

    public void setRtsc_port(rtsc_Port rtsc_port) {
        this.rtsc_port = rtsc_port;
    }
    public rtsc_Port getRtsc_port() {
        return rtsc_port;
    }

    public void setRtsc_port(rtsc_Port rtsc_port) {
        this.rtsc_port = rtsc_port;
    }
    public List<rtsc_MessageType> getRtsc_messagetypes() {
        return rtsc_messagetypes;
    }

    public void addRtsc_messagetype(Rtsc_messagetype rtsc_messagetype) {
        this.rtsc_messagetypes.add(rtsc_messagetype);
    }

}