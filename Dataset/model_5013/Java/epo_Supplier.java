





import java.util.List;
import java.util.ArrayList;

public class epo_Supplier  {

    private String name;





    private List<epo_PurchaseOrder> epo_purchaseorders;




    private List<epo_Customer> epo_customers;




    private List<epo_PurchaseOrder> epo_purchaseorders;




    private List<epo_PurchaseOrder> epo_purchaseorders;


    public epo_Supplier(
        String name    ) {
        this.name = name;
        this.epo_purchaseorders = new ArrayList<>();
        this.epo_customers = new ArrayList<>();
        this.epo_purchaseorders = new ArrayList<>();
        this.epo_purchaseorders = new ArrayList<>();
    }

    public epo_Supplier(
        String name        ArrayList<epo_PurchaseOrder> epo_purchaseorders,        ArrayList<epo_Customer> epo_customers,        ArrayList<epo_PurchaseOrder> epo_purchaseorders,        ArrayList<epo_PurchaseOrder> epo_purchaseorders    ) {
        this.name = name;
        this.epo_purchaseorders = epo_purchaseorders;
        this.epo_customers = epo_customers;
        this.epo_purchaseorders = epo_purchaseorders;
        this.epo_purchaseorders = epo_purchaseorders;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<epo_PurchaseOrder> getEpo_purchaseorders() {
        return epo_purchaseorders;
    }

    public void addEpo_purchaseorder(Epo_purchaseorder epo_purchaseorder) {
        this.epo_purchaseorders.add(epo_purchaseorder);
    }
    public List<epo_Customer> getEpo_customers() {
        return epo_customers;
    }

    public void addEpo_customer(Epo_customer epo_customer) {
        this.epo_customers.add(epo_customer);
    }
    public List<epo_PurchaseOrder> getEpo_purchaseorders() {
        return epo_purchaseorders;
    }

    public void addEpo_purchaseorder(Epo_purchaseorder epo_purchaseorder) {
        this.epo_purchaseorders.add(epo_purchaseorder);
    }
    public List<epo_PurchaseOrder> getEpo_purchaseorders() {
        return epo_purchaseorders;
    }

    public void addEpo_purchaseorder(Epo_purchaseorder epo_purchaseorder) {
        this.epo_purchaseorders.add(epo_purchaseorder);
    }

}