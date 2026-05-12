





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String managerId;
    private String leavesTaken;
    private int jobLevel;
    private String password;
    private int noOfLeaves;
    private String employeeName;
    private String employeeId;



    public Employee(
        String managerId,        String leavesTaken,        int jobLevel,        String password,        int noOfLeaves,        String employeeName,        String employeeId    ) {
        this.managerId = managerId;
        this.leavesTaken = leavesTaken;
        this.jobLevel = jobLevel;
        this.password = password;
        this.noOfLeaves = noOfLeaves;
        this.employeeName = employeeName;
        this.employeeId = employeeId;
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
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }


}