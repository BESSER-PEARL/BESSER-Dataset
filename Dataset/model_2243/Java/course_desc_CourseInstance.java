





import java.util.List;
import java.util.ArrayList;

public class course_desc_CourseInstance  {

    private int Year;
    private float LectureHours;
    private float LabHours;





    private course_desc_Lecturer course_desc_lecturer;




    private course_desc_CourseCoordinator course_desc_coursecoordinator;




    private course_desc_Course course_desc_course;




    private List<course_desc_CourseCoordinator> course_desc_coursecoordinators;




    private List<course_desc_Lecturer> course_desc_lecturers;




    private course_desc_Course course_desc_course;


    public course_desc_CourseInstance(
        int Year,        float LectureHours,        float LabHours    ) {
        this.Year = Year;
        this.LectureHours = LectureHours;
        this.LabHours = LabHours;
        this.course_desc_coursecoordinators = new ArrayList<>();
        this.course_desc_lecturers = new ArrayList<>();
    }

    public course_desc_CourseInstance(
        int Year,        float LectureHours,        float LabHours        ArrayList<course_desc_CourseCoordinator> course_desc_coursecoordinators,        ArrayList<course_desc_Lecturer> course_desc_lecturers    ) {
        this.Year = Year;
        this.LectureHours = LectureHours;
        this.LabHours = LabHours;
        this.course_desc_coursecoordinators = course_desc_coursecoordinators;
        this.course_desc_lecturers = course_desc_lecturers;
    }

    public int getYear() {
        return Year;
    }

    public void setYear(int Year) {
        this.Year = Year;
    }
    public float getLecturehours() {
        return LectureHours;
    }

    public void setLecturehours(float LectureHours) {
        this.LectureHours = LectureHours;
    }
    public float getLabhours() {
        return LabHours;
    }

    public void setLabhours(float LabHours) {
        this.LabHours = LabHours;
    }

    public course_desc_Lecturer getCourse_desc_lecturer() {
        return course_desc_lecturer;
    }

    public void setCourse_desc_lecturer(course_desc_Lecturer course_desc_lecturer) {
        this.course_desc_lecturer = course_desc_lecturer;
    }
    public course_desc_CourseCoordinator getCourse_desc_coursecoordinator() {
        return course_desc_coursecoordinator;
    }

    public void setCourse_desc_coursecoordinator(course_desc_CourseCoordinator course_desc_coursecoordinator) {
        this.course_desc_coursecoordinator = course_desc_coursecoordinator;
    }
    public course_desc_Course getCourse_desc_course() {
        return course_desc_course;
    }

    public void setCourse_desc_course(course_desc_Course course_desc_course) {
        this.course_desc_course = course_desc_course;
    }
    public List<course_desc_CourseCoordinator> getCourse_desc_coursecoordinators() {
        return course_desc_coursecoordinators;
    }

    public void addCourse_desc_coursecoordinator(Course_desc_coursecoordinator course_desc_coursecoordinator) {
        this.course_desc_coursecoordinators.add(course_desc_coursecoordinator);
    }
    public List<course_desc_Lecturer> getCourse_desc_lecturers() {
        return course_desc_lecturers;
    }

    public void addCourse_desc_lecturer(Course_desc_lecturer course_desc_lecturer) {
        this.course_desc_lecturers.add(course_desc_lecturer);
    }
    public course_desc_Course getCourse_desc_course() {
        return course_desc_course;
    }

    public void setCourse_desc_course(course_desc_Course course_desc_course) {
        this.course_desc_course = course_desc_course;
    }

}