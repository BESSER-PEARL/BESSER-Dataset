





import java.util.List;
import java.util.ArrayList;

public class tracker_EventAttributeSchema  {

    private String description;
    private String name;
    private String dataType;





    private tracker_EventSchema tracker_eventschema;


    public tracker_EventAttributeSchema(
        String description,        String name,        String dataType    ) {
        this.description = description;
        this.name = name;
        this.dataType = dataType;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public tracker_EventSchema getTracker_eventschema() {
        return tracker_eventschema;
    }

    public void setTracker_eventschema(tracker_EventSchema tracker_eventschema) {
        this.tracker_eventschema = tracker_eventschema;
    }

}