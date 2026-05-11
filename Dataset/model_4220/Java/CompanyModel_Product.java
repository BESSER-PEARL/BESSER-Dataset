





import java.util.List;
import java.util.ArrayList;

public class CompanyModel_Product  {

    private String name;
    private int productID;





    private CompanyModel_Department companymodel_department;


    public CompanyModel_Product(
        String name,        int productID    ) {
        this.name = name;
        this.productID = productID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getProductid() {
        return productID;
    }

    public void setProductid(int productID) {
        this.productID = productID;
    }

    public CompanyModel_Department getCompanymodel_department() {
        return companymodel_department;
    }

    public void setCompanymodel_department(CompanyModel_Department companymodel_department) {
        this.companymodel_department = companymodel_department;
    }

}