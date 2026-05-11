





import java.util.List;
import java.util.ArrayList;

public class extendedPO2_Supplier  {

    private String name;





    private List<extendedPO2_PurchaseOrder> extendedpo2_purchaseorders;




    private List<extendedPO2_PurchaseOrder> extendedpo2_purchaseorders;




    private List<extendedPO2_PurchaseOrder> extendedpo2_purchaseorders;




    private List<extendedPO2_Customer> extendedpo2_customers;


    public extendedPO2_Supplier(
        String name    ) {
        this.name = name;
        this.extendedpo2_purchaseorders = new ArrayList<>();
        this.extendedpo2_purchaseorders = new ArrayList<>();
        this.extendedpo2_purchaseorders = new ArrayList<>();
        this.extendedpo2_customers = new ArrayList<>();
    }

    public extendedPO2_Supplier(
        String name        ArrayList<extendedPO2_PurchaseOrder> extendedpo2_purchaseorders,        ArrayList<extendedPO2_PurchaseOrder> extendedpo2_purchaseorders,        ArrayList<extendedPO2_PurchaseOrder> extendedpo2_purchaseorders,        ArrayList<extendedPO2_Customer> extendedpo2_customers    ) {
        this.name = name;
        this.extendedpo2_purchaseorders = extendedpo2_purchaseorders;
        this.extendedpo2_purchaseorders = extendedpo2_purchaseorders;
        this.extendedpo2_purchaseorders = extendedpo2_purchaseorders;
        this.extendedpo2_customers = extendedpo2_customers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<extendedPO2_PurchaseOrder> getExtendedpo2_purchaseorders() {
        return extendedpo2_purchaseorders;
    }

    public void addExtendedpo2_purchaseorder(Extendedpo2_purchaseorder extendedpo2_purchaseorder) {
        this.extendedpo2_purchaseorders.add(extendedpo2_purchaseorder);
    }
    public List<extendedPO2_PurchaseOrder> getExtendedpo2_purchaseorders() {
        return extendedpo2_purchaseorders;
    }

    public void addExtendedpo2_purchaseorder(Extendedpo2_purchaseorder extendedpo2_purchaseorder) {
        this.extendedpo2_purchaseorders.add(extendedpo2_purchaseorder);
    }
    public List<extendedPO2_PurchaseOrder> getExtendedpo2_purchaseorders() {
        return extendedpo2_purchaseorders;
    }

    public void addExtendedpo2_purchaseorder(Extendedpo2_purchaseorder extendedpo2_purchaseorder) {
        this.extendedpo2_purchaseorders.add(extendedpo2_purchaseorder);
    }
    public List<extendedPO2_Customer> getExtendedpo2_customers() {
        return extendedpo2_customers;
    }

    public void addExtendedpo2_customer(Extendedpo2_customer extendedpo2_customer) {
        this.extendedpo2_customers.add(extendedpo2_customer);
    }

}