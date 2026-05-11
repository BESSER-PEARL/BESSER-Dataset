





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_composition_pc_av_EventChannel extends Entity {






    private List<composition_pc_av_EventChannelSinkConnector> composition_pc_av_eventchannelsinkconnectors;


    public pcm_pc_av_composition_pc_av_EventChannel(
    ) {
        super(
        );
        this.composition_pc_av_eventchannelsinkconnectors = new ArrayList<>();
    }

    public pcm_pc_av_composition_pc_av_EventChannel(
        ArrayList<composition_pc_av_EventChannelSinkConnector> composition_pc_av_eventchannelsinkconnectors    ) {
        this.composition_pc_av_eventchannelsinkconnectors = composition_pc_av_eventchannelsinkconnectors;
    }


    public List<composition_pc_av_EventChannelSinkConnector> getComposition_pc_av_eventchannelsinkconnectors() {
        return composition_pc_av_eventchannelsinkconnectors;
    }

    public void addComposition_pc_av_eventchannelsinkconnector(Composition_pc_av_eventchannelsinkconnector composition_pc_av_eventchannelsinkconnector) {
        this.composition_pc_av_eventchannelsinkconnectors.add(composition_pc_av_eventchannelsinkconnector);
    }

}