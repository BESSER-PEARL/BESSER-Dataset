





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_repository_av_pc_EventGroup extends Interface {






    private List<EventType> eventtypes;


    public pcm_av_pc_repository_av_pc_EventGroup(
    ) {
        super(
        );
        this.eventtypes = new ArrayList<>();
    }

    public pcm_av_pc_repository_av_pc_EventGroup(
        ArrayList<EventType> eventtypes    ) {
        this.eventtypes = eventtypes;
    }


    public List<EventType> getEventtypes() {
        return eventtypes;
    }

    public void addEventtype(Eventtype eventtype) {
        this.eventtypes.add(eventtype);
    }

}