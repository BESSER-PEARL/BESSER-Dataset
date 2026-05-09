





import java.util.List;
import java.util.ArrayList;

public class rtsc_MessageType extends NamedElement {






    private rtsc_MessageEvent rtsc_messageevent;




    private rtsc_MessageTypeRepository rtsc_messagetyperepository;




    private rtsc_Message rtsc_message;


    public rtsc_MessageType(
    ) {
        super(
        );
    }



    public rtsc_MessageEvent getRtsc_messageevent() {
        return rtsc_messageevent;
    }

    public void setRtsc_messageevent(rtsc_MessageEvent rtsc_messageevent) {
        this.rtsc_messageevent = rtsc_messageevent;
    }
    public rtsc_MessageTypeRepository getRtsc_messagetyperepository() {
        return rtsc_messagetyperepository;
    }

    public void setRtsc_messagetyperepository(rtsc_MessageTypeRepository rtsc_messagetyperepository) {
        this.rtsc_messagetyperepository = rtsc_messagetyperepository;
    }
    public rtsc_Message getRtsc_message() {
        return rtsc_message;
    }

    public void setRtsc_message(rtsc_Message rtsc_message) {
        this.rtsc_message = rtsc_message;
    }

}