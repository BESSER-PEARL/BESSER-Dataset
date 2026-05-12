





import java.util.List;
import java.util.ArrayList;

public class Session  {

    private String end;
    private String start;
    private None type;
    private None room;
    private int id;
    private String name;
    private None Events;



    public Session(
        String end,        String start,        None type,        None room,        int id,        String name,        None Events    ) {
        this.end = end;
        this.start = start;
        this.type = type;
        this.room = room;
        this.id = id;
        this.name = name;
        this.Events = Events;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public None getRoom() {
        return room;
    }

    public void setRoom(None room) {
        this.room = room;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getEvents() {
        return Events;
    }

    public void setEvents(None Events) {
        this.Events = Events;
    }


}