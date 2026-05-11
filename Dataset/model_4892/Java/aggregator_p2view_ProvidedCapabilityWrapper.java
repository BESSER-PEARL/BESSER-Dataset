





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_ProvidedCapabilityWrapper extends LabelProvider, p2_IProvidedCapability {






    private ProvidedCapability providedcapability;


    public aggregator_p2view_ProvidedCapabilityWrapper(
    ) {
        super(
        );
    }



    public ProvidedCapability getProvidedcapability() {
        return providedcapability;
    }

    public void setProvidedcapability(ProvidedCapability providedcapability) {
        this.providedcapability = providedcapability;
    }

}