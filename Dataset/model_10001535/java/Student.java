





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private None branch;
    private int semester;
    private String name;
    private int scholarNo;





    private Department department;




    private AcademicRecords academicrecords;


    public Student(
        None branch,        int semester,        String name,        int scholarNo    ) {
        this.branch = branch;
        this.semester = semester;
        this.name = name;
        this.scholarNo = scholarNo;
    }


    public None getBranch() {
        return branch;
    }

    public void setBranch(None branch) {
        this.branch = branch;
    }
    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getScholarno() {
        return scholarNo;
    }

    public void setScholarno(int scholarNo) {
        this.scholarNo = scholarNo;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    public AcademicRecords getAcademicrecords() {
        return academicrecords;
    }

    public void setAcademicrecords(AcademicRecords academicrecords) {
        this.academicrecords = academicrecords;
    }

}