





import java.util.List;
import java.util.ArrayList;

public class model1_SalesOrder extends Order {

    private int id;





    private model1_Company model1_company;




    private model1_ProductToOrder model1_producttoorder;




    private model1_Customer model1_customer;




    private model1_Customer model1_customer;


    public model1_SalesOrder(
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

    public model1_Company getModel1_company() {
        return model1_company;
    }

    public void setModel1_company(model1_Company model1_company) {
        this.model1_company = model1_company;
    }
    public model1_ProductToOrder getModel1_producttoorder() {
        return model1_producttoorder;
    }

    public void setModel1_producttoorder(model1_ProductToOrder model1_producttoorder) {
        this.model1_producttoorder = model1_producttoorder;
    }
    public model1_Customer getModel1_customer() {
        return model1_customer;
    }

    public void setModel1_customer(model1_Customer model1_customer) {
        this.model1_customer = model1_customer;
    }
    public model1_Customer getModel1_customer() {
        return model1_customer;
    }

    public void setModel1_customer(model1_Customer model1_customer) {
        this.model1_customer = model1_customer;
    }

}