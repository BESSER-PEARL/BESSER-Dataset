





import java.util.List;
import java.util.ArrayList;

public class universityextended_administration_Event  {

    private String title;





    private Time time;




    private Room room;


    public universityextended_administration_Event(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Time getTime() {
        return time;
    }

    public void setTime(Time time) {
        this.time = time;
    }
    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }

}