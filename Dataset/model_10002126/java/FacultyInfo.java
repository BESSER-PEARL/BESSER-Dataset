





import java.util.List;
import java.util.ArrayList;

public class FacultyInfo  {

    private String facultyID;
    private None department;
    private String facultyName;



    public FacultyInfo(
        String facultyID,        None department,        String facultyName    ) {
        this.facultyID = facultyID;
        this.department = department;
        this.facultyName = facultyName;
    }


    public String getFacultyid() {
        return facultyID;
    }

    public void setFacultyid(String facultyID) {
        this.facultyID = facultyID;
    }
    public None getDepartment() {
        return department;
    }

    public void setDepartment(None department) {
        this.department = department;
    }
    public String getFacultyname() {
        return facultyName;
    }

    public void setFacultyname(String facultyName) {
        this.facultyName = facultyName;
    }


}