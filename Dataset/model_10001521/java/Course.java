





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String courseName;
    private String subjectCode;





    private Department department;


    public Course(
        String courseName,        String subjectCode    ) {
        this.courseName = courseName;
        this.subjectCode = subjectCode;
    }


    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public String getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(String subjectCode) {
        this.subjectCode = subjectCode;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}