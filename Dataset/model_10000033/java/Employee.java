





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String leavesTaken;
    private String managerId;
    private String password;
    private String employeeId;
    private int noOfLeaves;
    private String employeeName;
    private int jobLevel;



    public Employee(
        String leavesTaken,        String managerId,        String password,        String employeeId,        int noOfLeaves,        String employeeName,        int jobLevel    ) {
        this.leavesTaken = leavesTaken;
        this.managerId = managerId;
        this.password = password;
        this.employeeId = employeeId;
        this.noOfLeaves = noOfLeaves;
        this.employeeName = employeeName;
        this.jobLevel = jobLevel;
    }


    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
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
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }
    public int getJoblevel() {
        return jobLevel;
    }

    public void setJoblevel(int jobLevel) {
        this.jobLevel = jobLevel;
    }


}