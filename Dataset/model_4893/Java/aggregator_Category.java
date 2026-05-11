





import java.util.List;
import java.util.ArrayList;

public class aggregator_Category extends MappedUnit {

    private String labelOverride;



    public aggregator_Category(
        String labelOverride    ) {
        super(
        );
        this.labelOverride = labelOverride;
    }


    public String getLabeloverride() {
        return labelOverride;
    }

    public void setLabeloverride(String labelOverride) {
        this.labelOverride = labelOverride;
    }


}