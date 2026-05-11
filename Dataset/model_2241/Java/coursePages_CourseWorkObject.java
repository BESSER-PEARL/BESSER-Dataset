




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class coursePages_CourseWorkObject  {

    private LocalDate start;
    private LocalDate end;
    private String room;
    private String day;
    private String courseWorkType;



    public coursePages_CourseWorkObject(
        LocalDate start,        LocalDate end,        String room,        String day,        String courseWorkType    ) {
        this.start = start;
        this.end = end;
        this.room = room;
        this.day = day;
        this.courseWorkType = courseWorkType;
    }


    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public LocalDate getEnd() {
        return end;
    }

    public void setEnd(LocalDate end) {
        this.end = end;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getCourseworktype() {
        return courseWorkType;
    }

    public void setCourseworktype(String courseWorkType) {
        this.courseWorkType = courseWorkType;
    }


}