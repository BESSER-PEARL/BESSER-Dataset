





import java.util.List;
import java.util.ArrayList;

public class oving4_TimeTableElement  {

    private String date;
    private int durationInMinutes;
    private String room;





    private oving4_CourseWork oving4_coursework;




    private oving4_TimeTable oving4_timetable;


    public oving4_TimeTableElement(
        String date,        int durationInMinutes,        String room    ) {
        this.date = date;
        this.durationInMinutes = durationInMinutes;
        this.room = room;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getDurationinminutes() {
        return durationInMinutes;
    }

    public void setDurationinminutes(int durationInMinutes) {
        this.durationInMinutes = durationInMinutes;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }

    public oving4_CourseWork getOving4_coursework() {
        return oving4_coursework;
    }

    public void setOving4_coursework(oving4_CourseWork oving4_coursework) {
        this.oving4_coursework = oving4_coursework;
    }
    public oving4_TimeTable getOving4_timetable() {
        return oving4_timetable;
    }

    public void setOving4_timetable(oving4_TimeTable oving4_timetable) {
        this.oving4_timetable = oving4_timetable;
    }

}