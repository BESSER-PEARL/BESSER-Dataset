





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int jobLevel;
    private String password;
    private String managerId;
    private String leavesTaken;
    private String employeeId;
    private int noOfLeaves;
    private String employeeName;



    public Employee(
        int jobLevel,        String password,        String managerId,        String leavesTaken,        String employeeId,        int noOfLeaves,        String employeeName    ) {
        this.jobLevel = jobLevel;
        this.password = password;
        this.managerId = managerId;
        this.leavesTaken = leavesTaken;
        this.employeeId = employeeId;
        this.noOfLeaves = noOfLeaves;
        this.employeeName = employeeName;
    }


    public int getJoblevel() {
        return jobLevel;
    }

    public void setJoblevel(int jobLevel) {
        this.jobLevel = jobLevel;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getManagerid() {
        return managerId;
    }

    public void setManagerid(String managerId) {
        this.managerId = managerId;
    }
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
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


}