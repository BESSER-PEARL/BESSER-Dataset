





import java.util.List;
import java.util.ArrayList;

public class toe_Project extends AllBase {

    private boolean departmentWide;
    private String name;





    private List<toe_Contribution> toe_contributions;




    private toe_Contribution toe_contribution;




    private List<toe_Employee> toe_employees;




    private toe_Employee toe_employee;


    public toe_Project(
        boolean departmentWide,        String name    ) {
        super(
        );
        this.departmentWide = departmentWide;
        this.name = name;
        this.toe_contributions = new ArrayList<>();
        this.toe_employees = new ArrayList<>();
    }

    public toe_Project(
        boolean departmentWide,        String name        ArrayList<toe_Contribution> toe_contributions,        ArrayList<toe_Employee> toe_employees    ) {
        this.departmentWide = departmentWide;
        this.name = name;
        this.toe_contributions = toe_contributions;
        this.toe_employees = toe_employees;
    }

    public boolean getDepartmentwide() {
        return departmentWide;
    }

    public void setDepartmentwide(boolean departmentWide) {
        this.departmentWide = departmentWide;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<toe_Contribution> getToe_contributions() {
        return toe_contributions;
    }

    public void addToe_contribution(Toe_contribution toe_contribution) {
        this.toe_contributions.add(toe_contribution);
    }
    public toe_Contribution getToe_contribution() {
        return toe_contribution;
    }

    public void setToe_contribution(toe_Contribution toe_contribution) {
        this.toe_contribution = toe_contribution;
    }
    public List<toe_Employee> getToe_employees() {
        return toe_employees;
    }

    public void addToe_employee(Toe_employee toe_employee) {
        this.toe_employees.add(toe_employee);
    }
    public toe_Employee getToe_employee() {
        return toe_employee;
    }

    public void setToe_employee(toe_Employee toe_employee) {
        this.toe_employee = toe_employee;
    }

}