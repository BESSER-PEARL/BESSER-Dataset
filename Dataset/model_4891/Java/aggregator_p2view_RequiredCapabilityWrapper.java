





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_RequiredCapabilityWrapper extends p2_IRequiredCapability, LabelProvider {






    private RequiredCapability requiredcapability;


    public aggregator_p2view_RequiredCapabilityWrapper(
    ) {
        super(
        );
    }



    public RequiredCapability getRequiredcapability() {
        return requiredcapability;
    }

    public void setRequiredcapability(RequiredCapability requiredcapability) {
        this.requiredcapability = requiredcapability;
    }

}