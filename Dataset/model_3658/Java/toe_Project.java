





import java.util.List;
import java.util.ArrayList;

public class toe_Project extends AllBase {

    private String name;
    private boolean departmentWide;





    private toe_Employee toe_employee;




    private List<toe_Employee> toe_employees;


    public toe_Project(
        String name,        boolean departmentWide    ) {
        super(
        );
        this.name = name;
        this.departmentWide = departmentWide;
        this.toe_employees = new ArrayList<>();
    }

    public toe_Project(
        String name,        boolean departmentWide        ArrayList<toe_Employee> toe_employees    ) {
        this.name = name;
        this.departmentWide = departmentWide;
        this.toe_employees = toe_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDepartmentwide() {
        return departmentWide;
    }

    public void setDepartmentwide(boolean departmentWide) {
        this.departmentWide = departmentWide;
    }

    public toe_Employee getToe_employee() {
        return toe_employee;
    }

    public void setToe_employee(toe_Employee toe_employee) {
        this.toe_employee = toe_employee;
    }
    public List<toe_Employee> getToe_employees() {
        return toe_employees;
    }

    public void addToe_employee(Toe_employee toe_employee) {
        this.toe_employees.add(toe_employee);
    }

}