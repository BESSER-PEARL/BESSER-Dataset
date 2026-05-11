





import java.util.List;
import java.util.ArrayList;

public class Demo_Department  {

    private boolean location;
    private int budget;
    private boolean name;





    private Demo_Employee demo_employee;




    private List<Demo_Employee> demo_employees;


    public Demo_Department(
        boolean location,        int budget,        boolean name    ) {
        this.location = location;
        this.budget = budget;
        this.name = name;
        this.demo_employees = new ArrayList<>();
    }

    public Demo_Department(
        boolean location,        int budget,        boolean name        ArrayList<Demo_Employee> demo_employees    ) {
        this.location = location;
        this.budget = budget;
        this.name = name;
        this.demo_employees = demo_employees;
    }

    public boolean getLocation() {
        return location;
    }

    public void setLocation(boolean location) {
        this.location = location;
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

    public Demo_Employee getDemo_employee() {
        return demo_employee;
    }

    public void setDemo_employee(Demo_Employee demo_employee) {
        this.demo_employee = demo_employee;
    }
    public List<Demo_Employee> getDemo_employees() {
        return demo_employees;
    }

    public void addDemo_employee(Demo_employee demo_employee) {
        this.demo_employees.add(demo_employee);
    }

}