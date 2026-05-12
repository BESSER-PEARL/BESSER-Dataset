





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String managerId;
    private String password;
    private String leavesTaken;
    private int jobLevel;
    private int noOfLeaves;
    private String employeeId;
    private String employeeName;



    public Employee(
        String managerId,        String password,        String leavesTaken,        int jobLevel,        int noOfLeaves,        String employeeId,        String employeeName    ) {
        this.managerId = managerId;
        this.password = password;
        this.leavesTaken = leavesTaken;
        this.jobLevel = jobLevel;
        this.noOfLeaves = noOfLeaves;
        this.employeeId = employeeId;
        this.employeeName = employeeName;
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
    public String getLeavestaken() {
        return leavesTaken;
    }

    public void setLeavestaken(String leavesTaken) {
        this.leavesTaken = leavesTaken;
    }
    public int getJoblevel() {
        return jobLevel;
    }

    public void setJoblevel(int jobLevel) {
        this.jobLevel = jobLevel;
    }
    public int getNoofleaves() {
        return noOfLeaves;
    }

    public void setNoofleaves(int noOfLeaves) {
        this.noOfLeaves = noOfLeaves;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
    }


}