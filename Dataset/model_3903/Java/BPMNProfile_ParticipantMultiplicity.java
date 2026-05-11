





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ParticipantMultiplicity extends BaseElement {

    private String maximum;
    private String minimum;



    public BPMNProfile_ParticipantMultiplicity(
        String maximum,        String minimum    ) {
        super(
        );
        this.maximum = maximum;
        this.minimum = minimum;
    }


    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }


}