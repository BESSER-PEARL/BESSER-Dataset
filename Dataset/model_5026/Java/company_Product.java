





import java.util.List;
import java.util.ArrayList;

public class company_Product  {

    private String description;
    private String vat;
    private float price;
    private String name;





    private List<company_OrderDetail> company_orderdetails;




    private company_OrderDetail company_orderdetail;




    private company_Category company_category;


    public company_Product(
        String description,        String vat,        float price,        String name    ) {
        this.description = description;
        this.vat = vat;
        this.price = price;
        this.name = name;
        this.company_orderdetails = new ArrayList<>();
    }

    public company_Product(
        String description,        String vat,        float price,        String name        ArrayList<company_OrderDetail> company_orderdetails    ) {
        this.description = description;
        this.vat = vat;
        this.price = price;
        this.name = name;
        this.company_orderdetails = company_orderdetails;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getVat() {
        return vat;
    }

    public void setVat(String vat) {
        this.vat = vat;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<company_OrderDetail> getCompany_orderdetails() {
        return company_orderdetails;
    }

    public void addCompany_orderdetail(Company_orderdetail company_orderdetail) {
        this.company_orderdetails.add(company_orderdetail);
    }
    public company_OrderDetail getCompany_orderdetail() {
        return company_orderdetail;
    }

    public void setCompany_orderdetail(company_OrderDetail company_orderdetail) {
        this.company_orderdetail = company_orderdetail;
    }
    public company_Category getCompany_category() {
        return company_category;
    }

    public void setCompany_category(company_Category company_category) {
        this.company_category = company_category;
    }

}