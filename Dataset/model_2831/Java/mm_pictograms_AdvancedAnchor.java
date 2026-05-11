





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_AdvancedAnchor extends Anchor {

    private boolean useAnchorLocationAsConnectionEndpoint;



    public mm_pictograms_AdvancedAnchor(
        boolean useAnchorLocationAsConnectionEndpoint    ) {
        super(
        );
        this.useAnchorLocationAsConnectionEndpoint = useAnchorLocationAsConnectionEndpoint;
    }


    public boolean getUseanchorlocationasconnectionendpoint() {
        return useAnchorLocationAsConnectionEndpoint;
    }

    public void setUseanchorlocationasconnectionendpoint(boolean useAnchorLocationAsConnectionEndpoint) {
        this.useAnchorLocationAsConnectionEndpoint = useAnchorLocationAsConnectionEndpoint;
    }


}