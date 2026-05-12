





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String courseName;
    private String Description;
    private String end_date;
    private int courseCode;
    private String start_date;





    private List<Student> students;




    private List<Student> students;


    public Course(
        String courseName,        String Description,        String end_date,        int courseCode,        String start_date    ) {
        this.courseName = courseName;
        this.Description = Description;
        this.end_date = end_date;
        this.courseCode = courseCode;
        this.start_date = start_date;
        this.students = new ArrayList<>();
        this.students = new ArrayList<>();
    }

    public Course(
        String courseName,        String Description,        String end_date,        int courseCode,        String start_date        ArrayList<Student> students,        ArrayList<Student> students    ) {
        this.courseName = courseName;
        this.Description = Description;
        this.end_date = end_date;
        this.courseCode = courseCode;
        this.start_date = start_date;
        this.students = students;
        this.students = students;
    }

    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getEnd_date() {
        return end_date;
    }

    public void setEnd_date(String end_date) {
        this.end_date = end_date;
    }
    public int getCoursecode() {
        return courseCode;
    }

    public void setCoursecode(int courseCode) {
        this.courseCode = courseCode;
    }
    public String getStart_date() {
        return start_date;
    }

    public void setStart_date(String start_date) {
        this.start_date = start_date;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}