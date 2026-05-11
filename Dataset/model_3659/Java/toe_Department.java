





import java.util.List;
import java.util.ArrayList;

public class toe_Department extends AllBase {

    private String name;





    private toe_Department toe_department;




    private toe_Employee toe_employee;




    private toe_Department toe_department;




    private List<toe_Employee> toe_employees;


    public toe_Department(
        String name    ) {
        super(
        );
        this.name = name;
        this.toe_employees = new ArrayList<>();
    }

    public toe_Department(
        String name        ArrayList<toe_Employee> toe_employees    ) {
        this.name = name;
        this.toe_employees = toe_employees;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public toe_Department getToe_department() {
        return toe_department;
    }

    public void setToe_department(toe_Department toe_department) {
        this.toe_department = toe_department;
    }
    public toe_Employee getToe_employee() {
        return toe_employee;
    }

    public void setToe_employee(toe_Employee toe_employee) {
        this.toe_employee = toe_employee;
    }
    public toe_Department getToe_department() {
        return toe_department;
    }

    public void setToe_department(toe_Department toe_department) {
        this.toe_department = toe_department;
    }
    public List<toe_Employee> getToe_employees() {
        return toe_employees;
    }

    public void addToe_employee(Toe_employee toe_employee) {
        this.toe_employees.add(toe_employee);
    }

}