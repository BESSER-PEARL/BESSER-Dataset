





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Event  {

    private String eventname;
    private int id;
    private int type;
    private String date;



    public Class_Diagram_for_Propsed_System_Event(
        String eventname,        int id,        int type,        String date    ) {
        this.eventname = eventname;
        this.id = id;
        this.type = type;
        this.date = date;
    }


    public String getEventname() {
        return eventname;
    }

    public void setEventname(String eventname) {
        this.eventname = eventname;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}