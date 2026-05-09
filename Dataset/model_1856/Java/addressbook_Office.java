





import java.util.List;
import java.util.ArrayList;

public class addressbook_Office extends Contact {

    private String company;



    public addressbook_Office(
        String company    ) {
        super(
        );
        this.company = company;
    }


    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }


}