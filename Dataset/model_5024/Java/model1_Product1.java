





import java.util.List;
import java.util.ArrayList;

public class model1_Product1  {

    private String vat;
    private String name;
    private String otherVATs;
    private String description;





    private model1_Category model1_category;




    private model1_OrderDetail model1_orderdetail;




    private List<model1_OrderDetail> model1_orderdetails;




    private model1_ProductToOrder model1_producttoorder;


    public model1_Product1(
        String vat,        String name,        String otherVATs,        String description    ) {
        this.vat = vat;
        this.name = name;
        this.otherVATs = otherVATs;
        this.description = description;
        this.model1_orderdetails = new ArrayList<>();
    }

    public model1_Product1(
        String vat,        String name,        String otherVATs,        String description        ArrayList<model1_OrderDetail> model1_orderdetails    ) {
        this.vat = vat;
        this.name = name;
        this.otherVATs = otherVATs;
        this.description = description;
        this.model1_orderdetails = model1_orderdetails;
    }

    public String getVat() {
        return vat;
    }

    public void setVat(String vat) {
        this.vat = vat;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOthervats() {
        return otherVATs;
    }

    public void setOthervats(String otherVATs) {
        this.otherVATs = otherVATs;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public model1_Category getModel1_category() {
        return model1_category;
    }

    public void setModel1_category(model1_Category model1_category) {
        this.model1_category = model1_category;
    }
    public model1_OrderDetail getModel1_orderdetail() {
        return model1_orderdetail;
    }

    public void setModel1_orderdetail(model1_OrderDetail model1_orderdetail) {
        this.model1_orderdetail = model1_orderdetail;
    }
    public List<model1_OrderDetail> getModel1_orderdetails() {
        return model1_orderdetails;
    }

    public void addModel1_orderdetail(Model1_orderdetail model1_orderdetail) {
        this.model1_orderdetails.add(model1_orderdetail);
    }
    public model1_ProductToOrder getModel1_producttoorder() {
        return model1_producttoorder;
    }

    public void setModel1_producttoorder(model1_ProductToOrder model1_producttoorder) {
        this.model1_producttoorder = model1_producttoorder;
    }

}