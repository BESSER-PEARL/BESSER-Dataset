





import java.util.List;
import java.util.ArrayList;

public class course_TimetableEntry  {

    private String day;
    private String type;
    private String room;
    private String time;





    private List<course_StudyProgram> course_studyprograms;




    private course_Timetable course_timetable;


    public course_TimetableEntry(
        String day,        String type,        String room,        String time    ) {
        this.day = day;
        this.type = type;
        this.room = room;
        this.time = time;
        this.course_studyprograms = new ArrayList<>();
    }

    public course_TimetableEntry(
        String day,        String type,        String room,        String time        ArrayList<course_StudyProgram> course_studyprograms    ) {
        this.day = day;
        this.type = type;
        this.room = room;
        this.time = time;
        this.course_studyprograms = course_studyprograms;
    }

    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public List<course_StudyProgram> getCourse_studyprograms() {
        return course_studyprograms;
    }

    public void addCourse_studyprogram(Course_studyprogram course_studyprogram) {
        this.course_studyprograms.add(course_studyprogram);
    }
    public course_Timetable getCourse_timetable() {
        return course_timetable;
    }

    public void setCourse_timetable(course_Timetable course_timetable) {
        this.course_timetable = course_timetable;
    }

}