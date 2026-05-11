





import java.util.List;
import java.util.ArrayList;

public class company_Employee extends Subunit {

    private float salary;





    private company_Person company_person;




    private company_Dept company_dept;


    public company_Employee(
        float salary    ) {
        super(
        );
        this.salary = salary;
    }


    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }

    public company_Person getCompany_person() {
        return company_person;
    }

    public void setCompany_person(company_Person company_person) {
        this.company_person = company_person;
    }
    public company_Dept getCompany_dept() {
        return company_dept;
    }

    public void setCompany_dept(company_Dept company_dept) {
        this.company_dept = company_dept;
    }

}