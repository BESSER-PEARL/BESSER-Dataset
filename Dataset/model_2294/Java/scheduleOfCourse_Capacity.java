





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_Capacity  {

    private int normal;
    private int exam;





    private scheduleOfCourse_Room scheduleofcourse_room;


    public scheduleOfCourse_Capacity(
        int normal,        int exam    ) {
        this.normal = normal;
        this.exam = exam;
    }


    public int getNormal() {
        return normal;
    }

    public void setNormal(int normal) {
        this.normal = normal;
    }
    public int getExam() {
        return exam;
    }

    public void setExam(int exam) {
        this.exam = exam;
    }

    public scheduleOfCourse_Room getScheduleofcourse_room() {
        return scheduleofcourse_room;
    }

    public void setScheduleofcourse_room(scheduleOfCourse_Room scheduleofcourse_room) {
        this.scheduleofcourse_room = scheduleofcourse_room;
    }

}