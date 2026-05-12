





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String leavesTaken;
    private String branch;
    private String studentName;
    private String password;
    private String studentId;
    private int year;



    public Student(
        String leavesTaken,        String branch,        String studentName,        String password,        String studentId,        int year    ) {
        this.leavesTaken = leavesTaken;
        this.branch = branch;
        this.studentName = studentName;
        this.password = password;
        this.studentId = studentId;
        this.year = year;
    }


    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public String getStudentname() {
        return studentName;
    }

    public void setStudentname(String studentName) {
        this.studentName = studentName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}