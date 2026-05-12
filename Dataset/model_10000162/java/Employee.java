





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String managerId;
    private int noOfLeaves;
    private String leavesTaken;
    private String employeeName;
    private String password;
    private String employeeId;
    private int jobLevel;



    public Employee(
        String managerId,        int noOfLeaves,        String leavesTaken,        String employeeName,        String password,        String employeeId,        int jobLevel    ) {
        this.managerId = managerId;
        this.noOfLeaves = noOfLeaves;
        this.leavesTaken = leavesTaken;
        this.employeeName = employeeName;
        this.password = password;
        this.employeeId = employeeId;
        this.jobLevel = jobLevel;
    }


    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public int getJoblevel() {
        return jobLevel;
    }

    public void setJoblevel(int jobLevel) {
        this.jobLevel = jobLevel;
    }


}