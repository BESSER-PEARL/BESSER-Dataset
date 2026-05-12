





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Event  {

    private String id;
    private int type;
    private String eventname;
    private String date;



    public Class_Diagram_for_Propsed_System_Event(
        String id,        int type,        String eventname,        String date    ) {
        this.id = id;
        this.type = type;
        this.eventname = eventname;
        this.date = date;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getEventname() {
        return eventname;
    }

    public void setEventname(String eventname) {
        this.eventname = eventname;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}