





import java.util.List;
import java.util.ArrayList;

public class model1_Company extends Address {






    private List<model1_Supplier> model1_suppliers;




    private List<model1_Customer> model1_customers;




    private List<model1_SalesOrder> model1_salesorders;




    private List<model1_PurchaseOrder> model1_purchaseorders;


    public model1_Company(
    ) {
        super(
        );
        this.model1_suppliers = new ArrayList<>();
        this.model1_customers = new ArrayList<>();
        this.model1_salesorders = new ArrayList<>();
        this.model1_purchaseorders = new ArrayList<>();
    }

    public model1_Company(
        ArrayList<model1_Supplier> model1_suppliers,        ArrayList<model1_Customer> model1_customers,        ArrayList<model1_SalesOrder> model1_salesorders,        ArrayList<model1_PurchaseOrder> model1_purchaseorders    ) {
        this.model1_suppliers = model1_suppliers;
        this.model1_customers = model1_customers;
        this.model1_salesorders = model1_salesorders;
        this.model1_purchaseorders = model1_purchaseorders;
    }


    public List<model1_Supplier> getModel1_suppliers() {
        return model1_suppliers;
    }

    public void addModel1_supplier(Model1_supplier model1_supplier) {
        this.model1_suppliers.add(model1_supplier);
    }
    public List<model1_Customer> getModel1_customers() {
        return model1_customers;
    }

    public void addModel1_customer(Model1_customer model1_customer) {
        this.model1_customers.add(model1_customer);
    }
    public List<model1_SalesOrder> getModel1_salesorders() {
        return model1_salesorders;
    }

    public void addModel1_salesorder(Model1_salesorder model1_salesorder) {
        this.model1_salesorders.add(model1_salesorder);
    }
    public List<model1_PurchaseOrder> getModel1_purchaseorders() {
        return model1_purchaseorders;
    }

    public void addModel1_purchaseorder(Model1_purchaseorder model1_purchaseorder) {
        this.model1_purchaseorders.add(model1_purchaseorder);
    }

}