





import java.util.List;
import java.util.ArrayList;

public class _101companies_Department  {

    private String name;
    private float totalSalary;





    private _101companies_Department _101companies_department;


    public _101companies_Department(
        String name,        float totalSalary    ) {
        this.name = name;
        this.totalSalary = totalSalary;
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

    public _101companies_Department get_101companies_department() {
        return _101companies_department;
    }

    public void set_101companies_department(_101companies_Department _101companies_department) {
        this._101companies_department = _101companies_department;
    }

}