





import java.util.List;
import java.util.ArrayList;

public class FacultyInfo  {

    private String facultyName;
    private None department;
    private String facultyID;



    public FacultyInfo(
        String facultyName,        None department,        String facultyID    ) {
        this.facultyName = facultyName;
        this.department = department;
        this.facultyID = facultyID;
    }


    public String getFacultyname() {
        return facultyName;
    }

    public void setFacultyname(String facultyName) {
        this.facultyName = facultyName;
    }
    public None getDepartment() {
        return department;
    }

    public void setDepartment(None department) {
        this.department = department;
    }
    public String getFacultyid() {
        return facultyID;
    }

    public void setFacultyid(String facultyID) {
        this.facultyID = facultyID;
    }


}