





import java.util.List;
import java.util.ArrayList;

public class company_Division  {

    private String budget;
    private String numberEmployeesOfTheMonth;
    private String name;





    private List<company_Department> company_departments;


    public company_Division(
        String budget,        String numberEmployeesOfTheMonth,        String name    ) {
        this.budget = budget;
        this.numberEmployeesOfTheMonth = numberEmployeesOfTheMonth;
        this.name = name;
        this.company_departments = new ArrayList<>();
    }

    public company_Division(
        String budget,        String numberEmployeesOfTheMonth,        String name        ArrayList<company_Department> company_departments    ) {
        this.budget = budget;
        this.numberEmployeesOfTheMonth = numberEmployeesOfTheMonth;
        this.name = name;
        this.company_departments = company_departments;
    }

    public String getBudget() {
        return budget;
    }

    public void setBudget(String budget) {
        this.budget = budget;
    }
    public String getNumberemployeesofthemonth() {
        return numberEmployeesOfTheMonth;
    }

    public void setNumberemployeesofthemonth(String numberEmployeesOfTheMonth) {
        this.numberEmployeesOfTheMonth = numberEmployeesOfTheMonth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<company_Department> getCompany_departments() {
        return company_departments;
    }

    public void addCompany_department(Company_department company_department) {
        this.company_departments.add(company_department);
    }

}