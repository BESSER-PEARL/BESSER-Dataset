





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ParticipantMultiplicity  {

    private int maximum;
    private int minimum;
    private String id;



    public bpmn2_ParticipantMultiplicity(
        int maximum,        int minimum,        String id    ) {
        this.maximum = maximum;
        this.minimum = minimum;
        this.id = id;
    }


    public int getMaximum() {
        return maximum;
    }

    public void setMaximum(int maximum) {
        this.maximum = maximum;
    }
    public int getMinimum() {
        return minimum;
    }

    public void setMinimum(int minimum) {
        this.minimum = minimum;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}