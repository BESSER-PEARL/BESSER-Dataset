





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IUpdateDescriptor  {

    private String description;
    private String id;
    private String range;
    private int severity;



    public aggregator_p2_IUpdateDescriptor(
        String description,        String id,        String range,        int severity    ) {
        this.description = description;
        this.id = id;
        this.range = range;
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


}