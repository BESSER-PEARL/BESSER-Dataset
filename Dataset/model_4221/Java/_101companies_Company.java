





import java.util.List;
import java.util.ArrayList;

public class _101companies_Company  {

    private String name;
    private float totalSalary;



    public _101companies_Company(
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


}