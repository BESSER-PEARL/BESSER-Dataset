





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_composition_av_pc_EventChannel extends Entity {






    private List<composition_av_pc_EventChannelSinkConnector> composition_av_pc_eventchannelsinkconnectors;


    public pcm_av_pc_composition_av_pc_EventChannel(
    ) {
        super(
        );
        this.composition_av_pc_eventchannelsinkconnectors = new ArrayList<>();
    }

    public pcm_av_pc_composition_av_pc_EventChannel(
        ArrayList<composition_av_pc_EventChannelSinkConnector> composition_av_pc_eventchannelsinkconnectors    ) {
        this.composition_av_pc_eventchannelsinkconnectors = composition_av_pc_eventchannelsinkconnectors;
    }


    public List<composition_av_pc_EventChannelSinkConnector> getComposition_av_pc_eventchannelsinkconnectors() {
        return composition_av_pc_eventchannelsinkconnectors;
    }

    public void addComposition_av_pc_eventchannelsinkconnector(Composition_av_pc_eventchannelsinkconnector composition_av_pc_eventchannelsinkconnector) {
        this.composition_av_pc_eventchannelsinkconnectors.add(composition_av_pc_eventchannelsinkconnector);
    }

}