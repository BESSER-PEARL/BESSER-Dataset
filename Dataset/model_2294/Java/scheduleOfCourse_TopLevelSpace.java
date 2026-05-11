





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_TopLevelSpace  {

    private String name;
    private String type;
    private String id;





    private scheduleOfCourse_Room scheduleofcourse_room;


    public scheduleOfCourse_TopLevelSpace(
        String name,        String type,        String id    ) {
        this.name = name;
        this.type = type;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public scheduleOfCourse_Room getScheduleofcourse_room() {
        return scheduleofcourse_room;
    }

    public void setScheduleofcourse_room(scheduleOfCourse_Room scheduleofcourse_room) {
        this.scheduleofcourse_room = scheduleofcourse_room;
    }

}