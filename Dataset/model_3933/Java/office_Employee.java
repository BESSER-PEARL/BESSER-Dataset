





import java.util.List;
import java.util.ArrayList;

public class office_Employee extends OfficeElement {

    private String title;





    private office_Employee office_employee;


    public office_Employee(
        String title    ) {
        super(
        );
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public office_Employee getOffice_employee() {
        return office_employee;
    }

    public void setOffice_employee(office_Employee office_employee) {
        this.office_employee = office_employee;
    }

}