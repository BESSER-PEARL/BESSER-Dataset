





import java.util.List;
import java.util.ArrayList;

public class courses_CourseHour  {

    private String startHour;
    private String type;
    private String day;
    private String room;
    private String endHour;





    private List<courses_StudyProgram> courses_studyprograms;


    public courses_CourseHour(
        String startHour,        String type,        String day,        String room,        String endHour    ) {
        this.startHour = startHour;
        this.type = type;
        this.day = day;
        this.room = room;
        this.endHour = endHour;
        this.courses_studyprograms = new ArrayList<>();
    }

    public courses_CourseHour(
        String startHour,        String type,        String day,        String room,        String endHour        ArrayList<courses_StudyProgram> courses_studyprograms    ) {
        this.startHour = startHour;
        this.type = type;
        this.day = day;
        this.room = room;
        this.endHour = endHour;
        this.courses_studyprograms = courses_studyprograms;
    }

    public String getStarthour() {
        return startHour;
    }

    public void setStarthour(String startHour) {
        this.startHour = startHour;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }
    public String getEndhour() {
        return endHour;
    }

    public void setEndhour(String endHour) {
        this.endHour = endHour;
    }

    public List<courses_StudyProgram> getCourses_studyprograms() {
        return courses_studyprograms;
    }

    public void addCourses_studyprogram(Courses_studyprogram courses_studyprogram) {
        this.courses_studyprograms.add(courses_studyprogram);
    }

}