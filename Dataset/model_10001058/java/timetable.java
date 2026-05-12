





import java.util.List;
import java.util.ArrayList;

public class timetable  {

    private int lectime;
    private String courseName;
    private int date;
    private int credithour;
    private int courseId;
    private String day;
    private String _attr;
    private String teacher;
    private int coursecode;





    private List<student> students;


    public timetable(
        int lectime,        String courseName,        int date,        int credithour,        int courseId,        String day,        String _attr,        String teacher,        int coursecode    ) {
        this.lectime = lectime;
        this.courseName = courseName;
        this.date = date;
        this.credithour = credithour;
        this.courseId = courseId;
        this.day = day;
        this._attr = _attr;
        this.teacher = teacher;
        this.coursecode = coursecode;
        this.students = new ArrayList<>();
    }

    public timetable(
        int lectime,        String courseName,        int date,        int credithour,        int courseId,        String day,        String _attr,        String teacher,        int coursecode        ArrayList<student> students    ) {
        this.lectime = lectime;
        this.courseName = courseName;
        this.date = date;
        this.credithour = credithour;
        this.courseId = courseId;
        this.day = day;
        this._attr = _attr;
        this.teacher = teacher;
        this.coursecode = coursecode;
        this.students = students;
    }

    public int getLectime() {
        return lectime;
    }

    public void setLectime(int lectime) {
        this.lectime = lectime;
    }
    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
    public int getCredithour() {
        return credithour;
    }

    public void setCredithour(int credithour) {
        this.credithour = credithour;
    }
    public int getCourseid() {
        return courseId;
    }

    public void setCourseid(int courseId) {
        this.courseId = courseId;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getTeacher() {
        return teacher;
    }

    public void setTeacher(String teacher) {
        this.teacher = teacher;
    }
    public int getCoursecode() {
        return coursecode;
    }

    public void setCoursecode(int coursecode) {
        this.coursecode = coursecode;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}