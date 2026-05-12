





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String studentId;
    private String password;
    private String leavesTaken;
    private String studentName;
    private int year;
    private String branch;



    public Student(
        String studentId,        String password,        String leavesTaken,        String studentName,        int year,        String branch    ) {
        this.studentId = studentId;
        this.password = password;
        this.leavesTaken = leavesTaken;
        this.studentName = studentName;
        this.year = year;
        this.branch = branch;
    }


    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public String getStudentname() {
        return studentName;
    }

    public void setStudentname(String studentName) {
        this.studentName = studentName;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }


}