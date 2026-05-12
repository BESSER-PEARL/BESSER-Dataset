





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String subjectCode;
    private String courseName;





    private Department department;


    public Course(
        String subjectCode,        String courseName    ) {
        this.subjectCode = subjectCode;
        this.courseName = courseName;
    }


    public String getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(String subjectCode) {
        this.subjectCode = subjectCode;
    }
    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}