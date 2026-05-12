





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String leavesTaken;
    private int jobLevel;
    private int noOfLeaves;
    private String password;
    private String employeeName;
    private String managerId;
    private String employeeId;



    public Employee(
        String leavesTaken,        int jobLevel,        int noOfLeaves,        String password,        String employeeName,        String managerId,        String employeeId    ) {
        this.leavesTaken = leavesTaken;
        this.jobLevel = jobLevel;
        this.noOfLeaves = noOfLeaves;
        this.password = password;
        this.employeeName = employeeName;
        this.managerId = managerId;
        this.employeeId = employeeId;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmployeename() {
        return employeeName;
    }

    public void setEmployeename(String employeeName) {
        this.employeeName = employeeName;
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


}