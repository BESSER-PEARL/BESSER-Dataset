





import java.util.List;
import java.util.ArrayList;

public class rtsc_MessageBuffer  {






    private rtsc_Port rtsc_port;




    private List<rtsc_Message> rtsc_messages;




    private List<rtsc_MessageType> rtsc_messagetypes;




    private rtsc_Port rtsc_port;


    public rtsc_MessageBuffer(
    ) {
        this.rtsc_messages = new ArrayList<>();
        this.rtsc_messagetypes = new ArrayList<>();
    }

    public rtsc_MessageBuffer(
        ArrayList<rtsc_Message> rtsc_messages,        ArrayList<rtsc_MessageType> rtsc_messagetypes    ) {
        this.rtsc_messages = rtsc_messages;
        this.rtsc_messagetypes = rtsc_messagetypes;
    }


    public rtsc_Port getRtsc_port() {
        return rtsc_port;
    }

    public void setRtsc_port(rtsc_Port rtsc_port) {
        this.rtsc_port = rtsc_port;
    }
    public List<rtsc_Message> getRtsc_messages() {
        return rtsc_messages;
    }

    public void addRtsc_message(Rtsc_message rtsc_message) {
        this.rtsc_messages.add(rtsc_message);
    }
    public List<rtsc_MessageType> getRtsc_messagetypes() {
        return rtsc_messagetypes;
    }

    public void addRtsc_messagetype(Rtsc_messagetype rtsc_messagetype) {
        this.rtsc_messagetypes.add(rtsc_messagetype);
    }
    public rtsc_Port getRtsc_port() {
        return rtsc_port;
    }

    public void setRtsc_port(rtsc_Port rtsc_port) {
        this.rtsc_port = rtsc_port;
    }

}