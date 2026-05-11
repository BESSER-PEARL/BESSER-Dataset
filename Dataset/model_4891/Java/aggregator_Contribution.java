





import java.util.List;
import java.util.ArrayList;

public class aggregator_Contribution extends StatusProvider, DescriptionProvider, InfosProvider, EnabledStatusProvider {

    private String label;



    public aggregator_Contribution(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}