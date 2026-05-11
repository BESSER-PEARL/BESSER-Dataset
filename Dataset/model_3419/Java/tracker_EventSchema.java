





import java.util.List;
import java.util.ArrayList;

public class tracker_EventSchema  {

    private String animalType;
    private String name;
    private String description;





    private tracker_GenericEvent tracker_genericevent;




    private tracker_Schema tracker_schema;


    public tracker_EventSchema(
        String animalType,        String name,        String description    ) {
        this.animalType = animalType;
        this.name = name;
        this.description = description;
    }


    public String getAnimaltype() {
        return animalType;
    }

    public void setAnimaltype(String animalType) {
        this.animalType = animalType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public tracker_GenericEvent getTracker_genericevent() {
        return tracker_genericevent;
    }

    public void setTracker_genericevent(tracker_GenericEvent tracker_genericevent) {
        this.tracker_genericevent = tracker_genericevent;
    }
    public tracker_Schema getTracker_schema() {
        return tracker_schema;
    }

    public void setTracker_schema(tracker_Schema tracker_schema) {
        this.tracker_schema = tracker_schema;
    }

}