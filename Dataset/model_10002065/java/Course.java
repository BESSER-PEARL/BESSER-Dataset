





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String CPrice;
    private String CInstructor;
    private String CCode;
    private String CName;





    private Department department;




    private Student student;




    private Admin admin;




    private Binary_File binary_file;


    public Course(
        String CPrice,        String CInstructor,        String CCode,        String CName    ) {
        this.CPrice = CPrice;
        this.CInstructor = CInstructor;
        this.CCode = CCode;
        this.CName = CName;
    }


    public String getCprice() {
        return CPrice;
    }

    public void setCprice(String CPrice) {
        this.CPrice = CPrice;
    }
    public String getCinstructor() {
        return CInstructor;
    }

    public void setCinstructor(String CInstructor) {
        this.CInstructor = CInstructor;
    }
    public String getCcode() {
        return CCode;
    }

    public void setCcode(String CCode) {
        this.CCode = CCode;
    }
    public String getCname() {
        return CName;
    }

    public void setCname(String CName) {
        this.CName = CName;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Binary_File getBinary_file() {
        return binary_file;
    }

    public void setBinary_file(Binary_File binary_file) {
        this.binary_file = binary_file;
    }

}