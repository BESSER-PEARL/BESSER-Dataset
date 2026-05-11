





import java.util.List;
import java.util.ArrayList;

public class courses_ExaminationPanel  {

    private String date;
    private String time;
    private String room;





    private courses_ExaminationArrangement courses_examinationarrangement;




    private List<courses_EvaluationForm> courses_evaluationforms;




    private courses_CourseInstance courses_courseinstance;


    public courses_ExaminationPanel(
        String date,        String time,        String room    ) {
        this.date = date;
        this.time = time;
        this.room = room;
        this.courses_evaluationforms = new ArrayList<>();
    }

    public courses_ExaminationPanel(
        String date,        String time,        String room        ArrayList<courses_EvaluationForm> courses_evaluationforms    ) {
        this.date = date;
        this.time = time;
        this.room = room;
        this.courses_evaluationforms = courses_evaluationforms;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }

    public courses_ExaminationArrangement getCourses_examinationarrangement() {
        return courses_examinationarrangement;
    }

    public void setCourses_examinationarrangement(courses_ExaminationArrangement courses_examinationarrangement) {
        this.courses_examinationarrangement = courses_examinationarrangement;
    }
    public List<courses_EvaluationForm> getCourses_evaluationforms() {
        return courses_evaluationforms;
    }

    public void addCourses_evaluationform(Courses_evaluationform courses_evaluationform) {
        this.courses_evaluationforms.add(courses_evaluationform);
    }
    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }

}