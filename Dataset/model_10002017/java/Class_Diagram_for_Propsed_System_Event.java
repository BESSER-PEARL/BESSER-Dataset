





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Event  {

    private int id;
    private String date;
    private int type;
    private String eventname;



    public Class_Diagram_for_Propsed_System_Event(
        int id,        String date,        int type,        String eventname    ) {
        this.id = id;
        this.date = date;
        this.type = type;
        this.eventname = eventname;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
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


}