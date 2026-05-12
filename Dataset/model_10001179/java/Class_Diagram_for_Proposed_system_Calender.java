





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Calender  {

    private String id;
    private String depid;
    private String eventType;
    private String author_id;





    private Class_Diagram_for_Proposed_system_Events class_diagram_for_proposed_system_events;


    public Class_Diagram_for_Proposed_system_Calender(
        String id,        String depid,        String eventType,        String author_id    ) {
        this.id = id;
        this.depid = depid;
        this.eventType = eventType;
        this.author_id = author_id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDepid() {
        return depid;
    }

    public void setDepid(String depid) {
        this.depid = depid;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getAuthor_id() {
        return author_id;
    }

    public void setAuthor_id(String author_id) {
        this.author_id = author_id;
    }

    public Class_Diagram_for_Proposed_system_Events getClass_diagram_for_proposed_system_events() {
        return class_diagram_for_proposed_system_events;
    }

    public void setClass_diagram_for_proposed_system_events(Class_Diagram_for_Proposed_system_Events class_diagram_for_proposed_system_events) {
        this.class_diagram_for_proposed_system_events = class_diagram_for_proposed_system_events;
    }

}