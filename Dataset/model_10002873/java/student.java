





import java.util.List;
import java.util.ArrayList;

public class student  {

    private String password;
    private String leavesTaken;
    private String studentName;
    private String studentId;
    private String branch;
    private int year;



    public student(
        String password,        String leavesTaken,        String studentName,        String studentId,        String branch,        int year    ) {
        this.password = password;
        this.leavesTaken = leavesTaken;
        this.studentName = studentName;
        this.studentId = studentId;
        this.branch = branch;
        this.year = year;
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
    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}