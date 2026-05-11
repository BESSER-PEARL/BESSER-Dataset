





import java.util.List;
import java.util.ArrayList;

public class coursePages_Course  {

    private String courseName;
    private String courseContent;
    private String courseCode;
    private float courseCredits;





    private List<coursePages_StudyPrograms> coursepages_studyprogramss;




    private coursePages_Student coursepages_student;




    private coursePages_StudyPrograms coursepages_studyprograms;


    public coursePages_Course(
        String courseName,        String courseContent,        String courseCode,        float courseCredits    ) {
        this.courseName = courseName;
        this.courseContent = courseContent;
        this.courseCode = courseCode;
        this.courseCredits = courseCredits;
        this.coursepages_studyprogramss = new ArrayList<>();
    }

    public coursePages_Course(
        String courseName,        String courseContent,        String courseCode,        float courseCredits        ArrayList<coursePages_StudyPrograms> coursepages_studyprogramss    ) {
        this.courseName = courseName;
        this.courseContent = courseContent;
        this.courseCode = courseCode;
        this.courseCredits = courseCredits;
        this.coursepages_studyprogramss = coursepages_studyprogramss;
    }

    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public String getCoursecontent() {
        return courseContent;
    }

    public void setCoursecontent(String courseContent) {
        this.courseContent = courseContent;
    }
    public String getCoursecode() {
        return courseCode;
    }

    public void setCoursecode(String courseCode) {
        this.courseCode = courseCode;
    }
    public float getCoursecredits() {
        return courseCredits;
    }

    public void setCoursecredits(float courseCredits) {
        this.courseCredits = courseCredits;
    }

    public List<coursePages_StudyPrograms> getCoursepages_studyprogramss() {
        return coursepages_studyprogramss;
    }

    public void addCoursepages_studyprograms(Coursepages_studyprograms coursepages_studyprograms) {
        this.coursepages_studyprogramss.add(coursepages_studyprograms);
    }
    public coursePages_Student getCoursepages_student() {
        return coursepages_student;
    }

    public void setCoursepages_student(coursePages_Student coursepages_student) {
        this.coursepages_student = coursepages_student;
    }
    public coursePages_StudyPrograms getCoursepages_studyprograms() {
        return coursepages_studyprograms;
    }

    public void setCoursepages_studyprograms(coursePages_StudyPrograms coursepages_studyprograms) {
        this.coursepages_studyprograms = coursepages_studyprograms;
    }

}