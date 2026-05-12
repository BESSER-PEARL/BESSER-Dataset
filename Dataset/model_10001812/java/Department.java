





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String description;
    private String departmentName;
    private int departmentID;





    private SessionManager sessionmanager;




    private Category category;




    private Department department;


    public Department(
        String description,        String departmentName,        int departmentID    ) {
        this.description = description;
        this.departmentName = departmentName;
        this.departmentID = departmentID;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDepartmentname() {
        return departmentName;
    }

    public void setDepartmentname(String departmentName) {
        this.departmentName = departmentName;
    }
    public int getDepartmentid() {
        return departmentID;
    }

    public void setDepartmentid(int departmentID) {
        this.departmentID = departmentID;
    }

    public SessionManager getSessionmanager() {
        return sessionmanager;
    }

    public void setSessionmanager(SessionManager sessionmanager) {
        this.sessionmanager = sessionmanager;
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}