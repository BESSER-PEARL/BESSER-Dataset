





import java.util.List;
import java.util.ArrayList;

public class coursePages_StudyPrograms  {

    private String studyProgramName;
    private String studyProgramCode;





    private coursePages_Student coursepages_student;




    private List<coursePages_Student> coursepages_students;


    public coursePages_StudyPrograms(
        String studyProgramName,        String studyProgramCode    ) {
        this.studyProgramName = studyProgramName;
        this.studyProgramCode = studyProgramCode;
        this.coursepages_students = new ArrayList<>();
    }

    public coursePages_StudyPrograms(
        String studyProgramName,        String studyProgramCode        ArrayList<coursePages_Student> coursepages_students    ) {
        this.studyProgramName = studyProgramName;
        this.studyProgramCode = studyProgramCode;
        this.coursepages_students = coursepages_students;
    }

    public String getStudyprogramname() {
        return studyProgramName;
    }

    public void setStudyprogramname(String studyProgramName) {
        this.studyProgramName = studyProgramName;
    }
    public String getStudyprogramcode() {
        return studyProgramCode;
    }

    public void setStudyprogramcode(String studyProgramCode) {
        this.studyProgramCode = studyProgramCode;
    }

    public coursePages_Student getCoursepages_student() {
        return coursepages_student;
    }

    public void setCoursepages_student(coursePages_Student coursepages_student) {
        this.coursepages_student = coursepages_student;
    }
    public List<coursePages_Student> getCoursepages_students() {
        return coursepages_students;
    }

    public void addCoursepages_student(Coursepages_student coursepages_student) {
        this.coursepages_students.add(coursepages_student);
    }

}