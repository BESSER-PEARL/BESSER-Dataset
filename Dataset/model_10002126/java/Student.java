





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private int scholarNo;
    private String name;
    private int semester;
    private None branch;





    private Department department;


    public Student(
        int scholarNo,        String name,        int semester,        None branch    ) {
        this.scholarNo = scholarNo;
        this.name = name;
        this.semester = semester;
        this.branch = branch;
    }


    public int getScholarno() {
        return scholarNo;
    }

    public void setScholarno(int scholarNo) {
        this.scholarNo = scholarNo;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }
    public None getBranch() {
        return branch;
    }

    public void setBranch(None branch) {
        this.branch = branch;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}