





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String deptId;
    private String deptName;





    private Instructor instructor;




    private Binary_File binary_file;


    public Department(
        String deptId,        String deptName    ) {
        this.deptId = deptId;
        this.deptName = deptName;
    }


    public String getDeptid() {
        return deptId;
    }

    public void setDeptid(String deptId) {
        this.deptId = deptId;
    }
    public String getDeptname() {
        return deptName;
    }

    public void setDeptname(String deptName) {
        this.deptName = deptName;
    }

    public Instructor getInstructor() {
        return instructor;
    }

    public void setInstructor(Instructor instructor) {
        this.instructor = instructor;
    }
    public Binary_File getBinary_file() {
        return binary_file;
    }

    public void setBinary_file(Binary_File binary_file) {
        this.binary_file = binary_file;
    }

}