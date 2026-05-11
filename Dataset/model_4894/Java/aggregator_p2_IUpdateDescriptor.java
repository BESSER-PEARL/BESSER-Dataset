





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IUpdateDescriptor  {

    private String range;
    private int severity;
    private String description;
    private String id;



    public aggregator_p2_IUpdateDescriptor(
        String range,        int severity,        String description,        String id    ) {
        this.range = range;
        this.severity = severity;
        this.description = description;
        this.id = id;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public int getSeverity() {
        return severity;
    }

    public void setSeverity(int severity) {
        this.severity = severity;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}