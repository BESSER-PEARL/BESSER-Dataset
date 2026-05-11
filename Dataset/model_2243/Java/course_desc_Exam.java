




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class course_desc_Exam extends Evaluation {

    private LocalDate date;
    private String place;
    private float duration;





    private List<course_desc_Student> course_desc_students;




    private course_desc_Student course_desc_student;




    private course_desc_Student course_desc_student;


    public course_desc_Exam(
        LocalDate date,        String place,        float duration    ) {
        super(
        );
        this.date = date;
        this.place = place;
        this.duration = duration;
        this.course_desc_students = new ArrayList<>();
    }

    public course_desc_Exam(
        LocalDate date,        String place,        float duration        ArrayList<course_desc_Student> course_desc_students    ) {
        this.date = date;
        this.place = place;
        this.duration = duration;
        this.course_desc_students = course_desc_students;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }
    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
    }

    public List<course_desc_Student> getCourse_desc_students() {
        return course_desc_students;
    }

    public void addCourse_desc_student(Course_desc_student course_desc_student) {
        this.course_desc_students.add(course_desc_student);
    }
    public course_desc_Student getCourse_desc_student() {
        return course_desc_student;
    }

    public void setCourse_desc_student(course_desc_Student course_desc_student) {
        this.course_desc_student = course_desc_student;
    }
    public course_desc_Student getCourse_desc_student() {
        return course_desc_student;
    }

    public void setCourse_desc_student(course_desc_Student course_desc_student) {
        this.course_desc_student = course_desc_student;
    }

}