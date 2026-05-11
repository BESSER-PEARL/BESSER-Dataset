




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class company_PurchaseOrder extends Order {

    private LocalDate date;





    private company_Supplier company_supplier;




    private company_Supplier company_supplier;




    private company_Company company_company;


    public company_PurchaseOrder(
        LocalDate date    ) {
        super(
        );
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public company_Supplier getCompany_supplier() {
        return company_supplier;
    }

    public void setCompany_supplier(company_Supplier company_supplier) {
        this.company_supplier = company_supplier;
    }
    public company_Supplier getCompany_supplier() {
        return company_supplier;
    }

    public void setCompany_supplier(company_Supplier company_supplier) {
        this.company_supplier = company_supplier;
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}