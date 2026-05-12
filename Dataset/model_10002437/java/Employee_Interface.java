





import java.util.List;
import java.util.ArrayList;

public class Employee_Interface  {






    private List<Department> departments;




    private Access_Information access_information;




    private Admin admin;


    public Employee_Interface(
    ) {
        this.departments = new ArrayList<>();
    }

    public Employee_Interface(
        ArrayList<Department> departments    ) {
        this.departments = departments;
    }


    public List<Department> getDepartments() {
        return departments;
    }

    public void addDepartment(Department department) {
        this.departments.add(department);
    }
    public Access_Information getAccess_information() {
        return access_information;
    }

    public void setAccess_information(Access_Information access_information) {
        this.access_information = access_information;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}