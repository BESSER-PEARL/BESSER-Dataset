





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Employee  {

    private int empid;
    private int post;
    private String id;
    private int shift;
    private int usergroup;
    private int user_id;
    private int depid;
    private int leavegroup;
    private int mobile;





    private Class_Diagram_for_Propsed_System_Posts class_diagram_for_propsed_system_posts;




    private List<Class_Diagram_for_Propsed_System_Deductions> class_diagram_for_propsed_system_deductionss;




    private List<Class_Diagram_for_Propsed_System_Attendance> class_diagram_for_propsed_system_attendances;




    private Class_Diagram_for_Propsed_System_Departments class_diagram_for_propsed_system_departments;




    private Class_Diagram_for_Propsed_System_Shifts class_diagram_for_propsed_system_shifts;




    private Class_Diagram_for_Propsed_System_Allowance class_diagram_for_propsed_system_allowance;


    public Class_Diagram_for_Propsed_System_Employee(
        int empid,        int post,        String id,        int shift,        int usergroup,        int user_id,        int depid,        int leavegroup,        int mobile    ) {
        this.empid = empid;
        this.post = post;
        this.id = id;
        this.shift = shift;
        this.usergroup = usergroup;
        this.user_id = user_id;
        this.depid = depid;
        this.leavegroup = leavegroup;
        this.mobile = mobile;
        this.class_diagram_for_propsed_system_deductionss = new ArrayList<>();
        this.class_diagram_for_propsed_system_attendances = new ArrayList<>();
    }

    public Class_Diagram_for_Propsed_System_Employee(
        int empid,        int post,        String id,        int shift,        int usergroup,        int user_id,        int depid,        int leavegroup,        int mobile        ArrayList<Class_Diagram_for_Propsed_System_Deductions> class_diagram_for_propsed_system_deductionss,        ArrayList<Class_Diagram_for_Propsed_System_Attendance> class_diagram_for_propsed_system_attendances    ) {
        this.empid = empid;
        this.post = post;
        this.id = id;
        this.shift = shift;
        this.usergroup = usergroup;
        this.user_id = user_id;
        this.depid = depid;
        this.leavegroup = leavegroup;
        this.mobile = mobile;
        this.class_diagram_for_propsed_system_deductionss = class_diagram_for_propsed_system_deductionss;
        this.class_diagram_for_propsed_system_attendances = class_diagram_for_propsed_system_attendances;
    }

    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }
    public int getPost() {
        return post;
    }

    public void setPost(int post) {
        this.post = post;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getShift() {
        return shift;
    }

    public void setShift(int shift) {
        this.shift = shift;
    }
    public int getUsergroup() {
        return usergroup;
    }

    public void setUsergroup(int usergroup) {
        this.usergroup = usergroup;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getDepid() {
        return depid;
    }

    public void setDepid(int depid) {
        this.depid = depid;
    }
    public int getLeavegroup() {
        return leavegroup;
    }

    public void setLeavegroup(int leavegroup) {
        this.leavegroup = leavegroup;
    }
    public int getMobile() {
        return mobile;
    }

    public void setMobile(int mobile) {
        this.mobile = mobile;
    }

    public Class_Diagram_for_Propsed_System_Posts getClass_diagram_for_propsed_system_posts() {
        return class_diagram_for_propsed_system_posts;
    }

    public void setClass_diagram_for_propsed_system_posts(Class_Diagram_for_Propsed_System_Posts class_diagram_for_propsed_system_posts) {
        this.class_diagram_for_propsed_system_posts = class_diagram_for_propsed_system_posts;
    }
    public List<Class_Diagram_for_Propsed_System_Deductions> getClass_diagram_for_propsed_system_deductionss() {
        return class_diagram_for_propsed_system_deductionss;
    }

    public void addClass_diagram_for_propsed_system_deductions(Class_diagram_for_propsed_system_deductions class_diagram_for_propsed_system_deductions) {
        this.class_diagram_for_propsed_system_deductionss.add(class_diagram_for_propsed_system_deductions);
    }
    public List<Class_Diagram_for_Propsed_System_Attendance> getClass_diagram_for_propsed_system_attendances() {
        return class_diagram_for_propsed_system_attendances;
    }

    public void addClass_diagram_for_propsed_system_attendance(Class_diagram_for_propsed_system_attendance class_diagram_for_propsed_system_attendance) {
        this.class_diagram_for_propsed_system_attendances.add(class_diagram_for_propsed_system_attendance);
    }
    public Class_Diagram_for_Propsed_System_Departments getClass_diagram_for_propsed_system_departments() {
        return class_diagram_for_propsed_system_departments;
    }

    public void setClass_diagram_for_propsed_system_departments(Class_Diagram_for_Propsed_System_Departments class_diagram_for_propsed_system_departments) {
        this.class_diagram_for_propsed_system_departments = class_diagram_for_propsed_system_departments;
    }
    public Class_Diagram_for_Propsed_System_Shifts getClass_diagram_for_propsed_system_shifts() {
        return class_diagram_for_propsed_system_shifts;
    }

    public void setClass_diagram_for_propsed_system_shifts(Class_Diagram_for_Propsed_System_Shifts class_diagram_for_propsed_system_shifts) {
        this.class_diagram_for_propsed_system_shifts = class_diagram_for_propsed_system_shifts;
    }
    public Class_Diagram_for_Propsed_System_Allowance getClass_diagram_for_propsed_system_allowance() {
        return class_diagram_for_propsed_system_allowance;
    }

    public void setClass_diagram_for_propsed_system_allowance(Class_Diagram_for_Propsed_System_Allowance class_diagram_for_propsed_system_allowance) {
        this.class_diagram_for_propsed_system_allowance = class_diagram_for_propsed_system_allowance;
    }

}