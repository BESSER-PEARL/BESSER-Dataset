





import java.util.List;
import java.util.ArrayList;

public class _101companies_Department  {

    private float totalSalary;
    private String name;





    private _101companies_Company _101companies_company;




    private _101companies_Department _101companies_department;


    public _101companies_Department(
        float totalSalary,        String name    ) {
        this.totalSalary = totalSalary;
        this.name = name;
    }


    public float getTotalsalary() {
        return totalSalary;
    }

    public void setTotalsalary(float totalSalary) {
        this.totalSalary = totalSalary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public _101companies_Company get_101companies_company() {
        return _101companies_company;
    }

    public void set_101companies_company(_101companies_Company _101companies_company) {
        this._101companies_company = _101companies_company;
    }
    public _101companies_Department get_101companies_department() {
        return _101companies_department;
    }

    public void set_101companies_department(_101companies_Department _101companies_department) {
        this._101companies_department = _101companies_department;
    }

}