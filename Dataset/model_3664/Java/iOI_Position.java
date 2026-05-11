





import java.util.List;
import java.util.ArrayList;

public class iOI_Position  {

    private String name;





    private iOI_Employee ioi_employee;




    private iOI_Company ioi_company;


    public iOI_Position(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iOI_Employee getIoi_employee() {
        return ioi_employee;
    }

    public void setIoi_employee(iOI_Employee ioi_employee) {
        this.ioi_employee = ioi_employee;
    }
    public iOI_Company getIoi_company() {
        return ioi_company;
    }

    public void setIoi_company(iOI_Company ioi_company) {
        this.ioi_company = ioi_company;
    }

}