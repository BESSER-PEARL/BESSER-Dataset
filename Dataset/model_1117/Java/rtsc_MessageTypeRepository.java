





import java.util.List;
import java.util.ArrayList;

public class rtsc_MessageTypeRepository  {






    private rtsc_System rtsc_system;




    private List<rtsc_MessageType> rtsc_messagetypes;


    public rtsc_MessageTypeRepository(
    ) {
        this.rtsc_messagetypes = new ArrayList<>();
    }

    public rtsc_MessageTypeRepository(
        ArrayList<rtsc_MessageType> rtsc_messagetypes    ) {
        this.rtsc_messagetypes = rtsc_messagetypes;
    }


    public rtsc_System getRtsc_system() {
        return rtsc_system;
    }

    public void setRtsc_system(rtsc_System rtsc_system) {
        this.rtsc_system = rtsc_system;
    }
    public List<rtsc_MessageType> getRtsc_messagetypes() {
        return rtsc_messagetypes;
    }

    public void addRtsc_messagetype(Rtsc_messagetype rtsc_messagetype) {
        this.rtsc_messagetypes.add(rtsc_messagetype);
    }

}