





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_composition_pc_ComposedStructure extends Entity {






    private List<composition_pc_Connector> composition_pc_connectors;




    private List<composition_pc_EventChannel> composition_pc_eventchannels;


    public pcm_pc_composition_pc_ComposedStructure(
    ) {
        super(
        );
        this.composition_pc_connectors = new ArrayList<>();
        this.composition_pc_eventchannels = new ArrayList<>();
    }

    public pcm_pc_composition_pc_ComposedStructure(
        ArrayList<composition_pc_Connector> composition_pc_connectors,        ArrayList<composition_pc_EventChannel> composition_pc_eventchannels    ) {
        this.composition_pc_connectors = composition_pc_connectors;
        this.composition_pc_eventchannels = composition_pc_eventchannels;
    }


    public List<composition_pc_Connector> getComposition_pc_connectors() {
        return composition_pc_connectors;
    }

    public void addComposition_pc_connector(Composition_pc_connector composition_pc_connector) {
        this.composition_pc_connectors.add(composition_pc_connector);
    }
    public List<composition_pc_EventChannel> getComposition_pc_eventchannels() {
        return composition_pc_eventchannels;
    }

    public void addComposition_pc_eventchannel(Composition_pc_eventchannel composition_pc_eventchannel) {
        this.composition_pc_eventchannels.add(composition_pc_eventchannel);
    }

}