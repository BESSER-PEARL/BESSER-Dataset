





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_composition_pc_EventChannel extends Entity {






    private List<composition_pc_EventChannelSourceConnector> composition_pc_eventchannelsourceconnectors;




    private List<composition_pc_EventChannelSinkConnector> composition_pc_eventchannelsinkconnectors;




    private EventGroup eventgroup;


    public pcm_pc_composition_pc_EventChannel(
    ) {
        super(
        );
        this.composition_pc_eventchannelsourceconnectors = new ArrayList<>();
        this.composition_pc_eventchannelsinkconnectors = new ArrayList<>();
    }

    public pcm_pc_composition_pc_EventChannel(
        ArrayList<composition_pc_EventChannelSourceConnector> composition_pc_eventchannelsourceconnectors,        ArrayList<composition_pc_EventChannelSinkConnector> composition_pc_eventchannelsinkconnectors    ) {
        this.composition_pc_eventchannelsourceconnectors = composition_pc_eventchannelsourceconnectors;
        this.composition_pc_eventchannelsinkconnectors = composition_pc_eventchannelsinkconnectors;
    }


    public List<composition_pc_EventChannelSourceConnector> getComposition_pc_eventchannelsourceconnectors() {
        return composition_pc_eventchannelsourceconnectors;
    }

    public void addComposition_pc_eventchannelsourceconnector(Composition_pc_eventchannelsourceconnector composition_pc_eventchannelsourceconnector) {
        this.composition_pc_eventchannelsourceconnectors.add(composition_pc_eventchannelsourceconnector);
    }
    public List<composition_pc_EventChannelSinkConnector> getComposition_pc_eventchannelsinkconnectors() {
        return composition_pc_eventchannelsinkconnectors;
    }

    public void addComposition_pc_eventchannelsinkconnector(Composition_pc_eventchannelsinkconnector composition_pc_eventchannelsinkconnector) {
        this.composition_pc_eventchannelsinkconnectors.add(composition_pc_eventchannelsinkconnector);
    }
    public EventGroup getEventgroup() {
        return eventgroup;
    }

    public void setEventgroup(EventGroup eventgroup) {
        this.eventgroup = eventgroup;
    }

}