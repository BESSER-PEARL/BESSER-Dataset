





import java.util.List;
import java.util.ArrayList;

public class Demo_Project  {

    private int budget;
    private boolean name;





    private Demo_Department demo_department;




    private List<Demo_Employee> demo_employees;




    private Demo_Employee demo_employee;




    private Demo_Department demo_department;


    public Demo_Project(
        int budget,        boolean name    ) {
        this.budget = budget;
        this.name = name;
        this.demo_employees = new ArrayList<>();
    }

    public Demo_Project(
        int budget,        boolean name        ArrayList<Demo_Employee> demo_employees    ) {
        this.budget = budget;
        this.name = name;
        this.demo_employees = demo_employees;
    }

    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }

    public Demo_Department getDemo_department() {
        return demo_department;
    }

    public void setDemo_department(Demo_Department demo_department) {
        this.demo_department = demo_department;
    }
    public List<Demo_Employee> getDemo_employees() {
        return demo_employees;
    }

    public void addDemo_employee(Demo_employee demo_employee) {
        this.demo_employees.add(demo_employee);
    }
    public Demo_Employee getDemo_employee() {
        return demo_employee;
    }

    public void setDemo_employee(Demo_Employee demo_employee) {
        this.demo_employee = demo_employee;
    }
    public Demo_Department getDemo_department() {
        return demo_department;
    }

    public void setDemo_department(Demo_Department demo_department) {
        this.demo_department = demo_department;
    }

}