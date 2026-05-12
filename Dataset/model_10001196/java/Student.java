





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String leavesTaken;
    private int noOfLeaves;
    private String studentName;
    private String password;
    private String studentId;



    public Student(
        String leavesTaken,        int noOfLeaves,        String studentName,        String password,        String studentId    ) {
        this.leavesTaken = leavesTaken;
        this.noOfLeaves = noOfLeaves;
        this.studentName = studentName;
        this.password = password;
        this.studentId = studentId;
    }


    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
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


}