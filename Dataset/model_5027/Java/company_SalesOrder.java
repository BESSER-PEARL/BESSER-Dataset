





import java.util.List;
import java.util.ArrayList;

public class company_SalesOrder extends Order {

    private int id;





    private company_Customer company_customer;




    private company_Company company_company;




    private company_Customer company_customer;


    public company_SalesOrder(
        int id    ) {
        super(
        );
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public company_Customer getCompany_customer() {
        return company_customer;
    }

    public void setCompany_customer(company_Customer company_customer) {
        this.company_customer = company_customer;
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }
    public company_Customer getCompany_customer() {
        return company_customer;
    }

    public void setCompany_customer(company_Customer company_customer) {
        this.company_customer = company_customer;
    }

}