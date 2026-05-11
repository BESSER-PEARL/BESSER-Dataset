





import java.util.List;
import java.util.ArrayList;

public class company_Person  {

    private String address;
    private String name;





    private company_Employee company_employee;


    public company_Person(
        String address,        String name    ) {
        this.address = address;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public company_Employee getCompany_employee() {
        return company_employee;
    }

    public void setCompany_employee(company_Employee company_employee) {
        this.company_employee = company_employee;
    }

}