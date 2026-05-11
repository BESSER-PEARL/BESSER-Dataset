





import java.util.List;
import java.util.ArrayList;

public class epo2_Supplier  {

    private String name;





    private List<epo2_PurchaseOrder> epo2_purchaseorders;




    private List<epo2_PurchaseOrder> epo2_purchaseorders;




    private List<epo2_Customer> epo2_customers;




    private List<epo2_PurchaseOrder> epo2_purchaseorders;


    public epo2_Supplier(
        String name    ) {
        this.name = name;
        this.epo2_purchaseorders = new ArrayList<>();
        this.epo2_purchaseorders = new ArrayList<>();
        this.epo2_customers = new ArrayList<>();
        this.epo2_purchaseorders = new ArrayList<>();
    }

    public epo2_Supplier(
        String name        ArrayList<epo2_PurchaseOrder> epo2_purchaseorders,        ArrayList<epo2_PurchaseOrder> epo2_purchaseorders,        ArrayList<epo2_Customer> epo2_customers,        ArrayList<epo2_PurchaseOrder> epo2_purchaseorders    ) {
        this.name = name;
        this.epo2_purchaseorders = epo2_purchaseorders;
        this.epo2_purchaseorders = epo2_purchaseorders;
        this.epo2_customers = epo2_customers;
        this.epo2_purchaseorders = epo2_purchaseorders;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<epo2_PurchaseOrder> getEpo2_purchaseorders() {
        return epo2_purchaseorders;
    }

    public void addEpo2_purchaseorder(Epo2_purchaseorder epo2_purchaseorder) {
        this.epo2_purchaseorders.add(epo2_purchaseorder);
    }
    public List<epo2_PurchaseOrder> getEpo2_purchaseorders() {
        return epo2_purchaseorders;
    }

    public void addEpo2_purchaseorder(Epo2_purchaseorder epo2_purchaseorder) {
        this.epo2_purchaseorders.add(epo2_purchaseorder);
    }
    public List<epo2_Customer> getEpo2_customers() {
        return epo2_customers;
    }

    public void addEpo2_customer(Epo2_customer epo2_customer) {
        this.epo2_customers.add(epo2_customer);
    }
    public List<epo2_PurchaseOrder> getEpo2_purchaseorders() {
        return epo2_purchaseorders;
    }

    public void addEpo2_purchaseorder(Epo2_purchaseorder epo2_purchaseorder) {
        this.epo2_purchaseorders.add(epo2_purchaseorder);
    }

}