





import java.util.List;
import java.util.ArrayList;

public class Plan  {

    private String Monthly_plan;
    private String day_plan;
    private String weekly_plan;





    private List<Employee> employees;


    public Plan(
        String Monthly_plan,        String day_plan,        String weekly_plan    ) {
        this.Monthly_plan = Monthly_plan;
        this.day_plan = day_plan;
        this.weekly_plan = weekly_plan;
        this.employees = new ArrayList<>();
    }

    public Plan(
        String Monthly_plan,        String day_plan,        String weekly_plan        ArrayList<Employee> employees    ) {
        this.Monthly_plan = Monthly_plan;
        this.day_plan = day_plan;
        this.weekly_plan = weekly_plan;
        this.employees = employees;
    }

    public String getMonthly_plan() {
        return Monthly_plan;
    }

    public void setMonthly_plan(String Monthly_plan) {
        this.Monthly_plan = Monthly_plan;
    }
    public String getDay_plan() {
        return day_plan;
    }

    public void setDay_plan(String day_plan) {
        this.day_plan = day_plan;
    }
    public String getWeekly_plan() {
        return weekly_plan;
    }

    public void setWeekly_plan(String weekly_plan) {
        this.weekly_plan = weekly_plan;
    }

    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}