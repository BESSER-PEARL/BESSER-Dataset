





import java.util.List;
import java.util.ArrayList;

public class Package_Employee  {

    private String shift;
    private String post;
    private int leavegroup;
    private int depid;
    private String empid;
    private String id;
    private int usergroup;





    private Package_Shifts package_shifts;




    private Package_Departments package_departments;




    private Package_Allowance package_allowance;




    private List<Package_Attendance> package_attendances;




    private Package_Posts package_posts;


    public Package_Employee(
        String shift,        String post,        int leavegroup,        int depid,        String empid,        String id,        int usergroup    ) {
        this.shift = shift;
        this.post = post;
        this.leavegroup = leavegroup;
        this.depid = depid;
        this.empid = empid;
        this.id = id;
        this.usergroup = usergroup;
        this.package_attendances = new ArrayList<>();
    }

    public Package_Employee(
        String shift,        String post,        int leavegroup,        int depid,        String empid,        String id,        int usergroup        ArrayList<Package_Attendance> package_attendances    ) {
        this.shift = shift;
        this.post = post;
        this.leavegroup = leavegroup;
        this.depid = depid;
        this.empid = empid;
        this.id = id;
        this.usergroup = usergroup;
        this.package_attendances = package_attendances;
    }

    public String getShift() {
        return shift;
    }

    public void setShift(String shift) {
        this.shift = shift;
    }
    public String getPost() {
        return post;
    }

    public void setPost(String post) {
        this.post = post;
    }
    public int getLeavegroup() {
        return leavegroup;
    }

    public void setLeavegroup(int leavegroup) {
        this.leavegroup = leavegroup;
    }
    public int getDepid() {
        return depid;
    }

    public void setDepid(int depid) {
        this.depid = depid;
    }
    public String getEmpid() {
        return empid;
    }

    public void setEmpid(String empid) {
        this.empid = empid;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getUsergroup() {
        return usergroup;
    }

    public void setUsergroup(int usergroup) {
        this.usergroup = usergroup;
    }

    public Package_Shifts getPackage_shifts() {
        return package_shifts;
    }

    public void setPackage_shifts(Package_Shifts package_shifts) {
        this.package_shifts = package_shifts;
    }
    public Package_Departments getPackage_departments() {
        return package_departments;
    }

    public void setPackage_departments(Package_Departments package_departments) {
        this.package_departments = package_departments;
    }
    public Package_Allowance getPackage_allowance() {
        return package_allowance;
    }

    public void setPackage_allowance(Package_Allowance package_allowance) {
        this.package_allowance = package_allowance;
    }
    public List<Package_Attendance> getPackage_attendances() {
        return package_attendances;
    }

    public void addPackage_attendance(Package_attendance package_attendance) {
        this.package_attendances.add(package_attendance);
    }
    public Package_Posts getPackage_posts() {
        return package_posts;
    }

    public void setPackage_posts(Package_Posts package_posts) {
        this.package_posts = package_posts;
    }

}