





import java.util.List;
import java.util.ArrayList;

public class _101companies_Company  {

    private String name;
    private float totalSalary;





    private List<_101companies_Department> _101companies_departments;


    public _101companies_Company(
        String name,        float totalSalary    ) {
        this.name = name;
        this.totalSalary = totalSalary;
        this._101companies_departments = new ArrayList<>();
    }

    public _101companies_Company(
        String name,        float totalSalary        ArrayList<_101companies_Department> _101companies_departments    ) {
        this.name = name;
        this.totalSalary = totalSalary;
        this._101companies_departments = _101companies_departments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getTotalsalary() {
        return totalSalary;
    }

    public void setTotalsalary(float totalSalary) {
        this.totalSalary = totalSalary;
    }

    public List<_101companies_Department> get_101companies_departments() {
        return _101companies_departments;
    }

    public void add_101companies_department(_101companies_department _101companies_department) {
        this._101companies_departments.add(_101companies_department);
    }

}