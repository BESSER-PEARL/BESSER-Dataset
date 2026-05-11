





import java.util.List;
import java.util.ArrayList;

public class model1_SalesOrder extends Order {

    private int id;





    private model1_Customer model1_customer;




    private model1_PurchaseOrder model1_purchaseorder;




    private List<model1_PurchaseOrder> model1_purchaseorders;




    private model1_Customer model1_customer;


    public model1_SalesOrder(
        int id    ) {
        super(
        );
        this.id = id;
        this.model1_purchaseorders = new ArrayList<>();
    }

    public model1_SalesOrder(
        int id        ArrayList<model1_PurchaseOrder> model1_purchaseorders    ) {
        this.id = id;
        this.model1_purchaseorders = model1_purchaseorders;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public model1_Customer getModel1_customer() {
        return model1_customer;
    }

    public void setModel1_customer(model1_Customer model1_customer) {
        this.model1_customer = model1_customer;
    }
    public model1_PurchaseOrder getModel1_purchaseorder() {
        return model1_purchaseorder;
    }

    public void setModel1_purchaseorder(model1_PurchaseOrder model1_purchaseorder) {
        this.model1_purchaseorder = model1_purchaseorder;
    }
    public List<model1_PurchaseOrder> getModel1_purchaseorders() {
        return model1_purchaseorders;
    }

    public void addModel1_purchaseorder(Model1_purchaseorder model1_purchaseorder) {
        this.model1_purchaseorders.add(model1_purchaseorder);
    }
    public model1_Customer getModel1_customer() {
        return model1_customer;
    }

    public void setModel1_customer(model1_Customer model1_customer) {
        this.model1_customer = model1_customer;
    }

}