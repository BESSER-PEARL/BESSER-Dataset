





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_Room  {

    private String type;
    private String id;
    private String description;
    private String name;





    private scheduleOfCourse_Lesson scheduleofcourse_lesson;




    private scheduleOfCourse_Shift scheduleofcourse_shift;


    public scheduleOfCourse_Room(
        String type,        String id,        String description,        String name    ) {
        this.type = type;
        this.id = id;
        this.description = description;
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

    public scheduleOfCourse_Lesson getScheduleofcourse_lesson() {
        return scheduleofcourse_lesson;
    }

    public void setScheduleofcourse_lesson(scheduleOfCourse_Lesson scheduleofcourse_lesson) {
        this.scheduleofcourse_lesson = scheduleofcourse_lesson;
    }
    public scheduleOfCourse_Shift getScheduleofcourse_shift() {
        return scheduleofcourse_shift;
    }

    public void setScheduleofcourse_shift(scheduleOfCourse_Shift scheduleofcourse_shift) {
        this.scheduleofcourse_shift = scheduleofcourse_shift;
    }

}