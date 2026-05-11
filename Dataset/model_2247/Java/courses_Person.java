





import java.util.List;
import java.util.ArrayList;

public class courses_Person  {

    private String name;
    private float Credits;





    private courses_Course courses_course;




    private courses_University courses_university;




    private List<courses_Course> courses_courses;




    private courses_StudyProgram courses_studyprogram;




    private courses_University courses_university;




    private courses_StudyProgram courses_studyprogram;


    public courses_Person(
        String name,        float Credits    ) {
        this.name = name;
        this.Credits = Credits;
        this.courses_courses = new ArrayList<>();
    }

    public courses_Person(
        String name,        float Credits        ArrayList<courses_Course> courses_courses    ) {
        this.name = name;
        this.Credits = Credits;
        this.courses_courses = courses_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getCredits() {
        return Credits;
    }

    public void setCredits(float Credits) {
        this.Credits = Credits;
    }

    public courses_Course getCourses_course() {
        return courses_course;
    }

    public void setCourses_course(courses_Course courses_course) {
        this.courses_course = courses_course;
    }
    public courses_University getCourses_university() {
        return courses_university;
    }

    public void setCourses_university(courses_University courses_university) {
        this.courses_university = courses_university;
    }
    public List<courses_Course> getCourses_courses() {
        return courses_courses;
    }

    public void addCourses_course(Courses_course courses_course) {
        this.courses_courses.add(courses_course);
    }
    public courses_StudyProgram getCourses_studyprogram() {
        return courses_studyprogram;
    }

    public void setCourses_studyprogram(courses_StudyProgram courses_studyprogram) {
        this.courses_studyprogram = courses_studyprogram;
    }
    public courses_University getCourses_university() {
        return courses_university;
    }

    public void setCourses_university(courses_University courses_university) {
        this.courses_university = courses_university;
    }
    public courses_StudyProgram getCourses_studyprogram() {
        return courses_studyprogram;
    }

    public void setCourses_studyprogram(courses_StudyProgram courses_studyprogram) {
        this.courses_studyprogram = courses_studyprogram;
    }

}