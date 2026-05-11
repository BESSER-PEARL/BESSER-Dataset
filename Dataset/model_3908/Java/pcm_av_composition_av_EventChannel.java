





import java.util.List;
import java.util.ArrayList;

public class pcm_av_composition_av_EventChannel extends Entity {






    private List<composition_av_EventChannelSinkConnector> composition_av_eventchannelsinkconnectors;


    public pcm_av_composition_av_EventChannel(
    ) {
        super(
        );
        this.composition_av_eventchannelsinkconnectors = new ArrayList<>();
    }

    public pcm_av_composition_av_EventChannel(
        ArrayList<composition_av_EventChannelSinkConnector> composition_av_eventchannelsinkconnectors    ) {
        this.composition_av_eventchannelsinkconnectors = composition_av_eventchannelsinkconnectors;
    }


    public List<composition_av_EventChannelSinkConnector> getComposition_av_eventchannelsinkconnectors() {
        return composition_av_eventchannelsinkconnectors;
    }

    public void addComposition_av_eventchannelsinkconnector(Composition_av_eventchannelsinkconnector composition_av_eventchannelsinkconnector) {
        this.composition_av_eventchannelsinkconnectors.add(composition_av_eventchannelsinkconnector);
    }

}