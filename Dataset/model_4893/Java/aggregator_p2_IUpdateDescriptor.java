





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IUpdateDescriptor  {

    private String description;
    private String range;
    private String id;
    private int severity;



    public aggregator_p2_IUpdateDescriptor(
        String description,        String range,        String id,        int severity    ) {
        this.description = description;
        this.range = range;
        this.id = id;
        this.severity = severity;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getSeverity() {
        return severity;
    }

    public void setSeverity(int severity) {
        this.severity = severity;
    }


}