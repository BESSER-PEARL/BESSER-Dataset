





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String name;
    private None branch;
    private int scholarNo;
    private int semester;





    private AcademicRecords academicrecords;




    private Department department;


    public Student(
        String name,        None branch,        int scholarNo,        int semester    ) {
        this.name = name;
        this.branch = branch;
        this.scholarNo = scholarNo;
        this.semester = semester;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getBranch() {
        return branch;
    }

    public void setBranch(None branch) {
        this.branch = branch;
    }
    public int getScholarno() {
        return scholarNo;
    }

    public void setScholarno(int scholarNo) {
        this.scholarNo = scholarNo;
    }
    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }

    public AcademicRecords getAcademicrecords() {
        return academicrecords;
    }

    public void setAcademicrecords(AcademicRecords academicrecords) {
        this.academicrecords = academicrecords;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}