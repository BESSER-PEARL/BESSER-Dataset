





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String managerId;
    private String employeeId;
    private String password;
    private int noOfLeaves;
    private String employeeName;
    private int jobLevel;
    private String leavesTaken;



    public Employee(
        String managerId,        String employeeId,        String password,        int noOfLeaves,        String employeeName,        int jobLevel,        String leavesTaken    ) {
        this.managerId = managerId;
        this.employeeId = employeeId;
        this.password = password;
        this.noOfLeaves = noOfLeaves;
        this.employeeName = employeeName;
        this.jobLevel = jobLevel;
        this.leavesTaken = leavesTaken;
    }


    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }


}