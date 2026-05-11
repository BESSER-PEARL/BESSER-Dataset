





import java.util.List;
import java.util.ArrayList;

public class epo2_Customer  {

    private int customerID;





    private epo2_PurchaseOrder epo2_purchaseorder;




    private epo2_Supplier epo2_supplier;




    private List<epo2_PurchaseOrder> epo2_purchaseorders;


    public epo2_Customer(
        int customerID    ) {
        this.customerID = customerID;
        this.epo2_purchaseorders = new ArrayList<>();
    }

    public epo2_Customer(
        int customerID        ArrayList<epo2_PurchaseOrder> epo2_purchaseorders    ) {
        this.customerID = customerID;
        this.epo2_purchaseorders = epo2_purchaseorders;
    }

    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }

    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }
    public epo2_Supplier getEpo2_supplier() {
        return epo2_supplier;
    }

    public void setEpo2_supplier(epo2_Supplier epo2_supplier) {
        this.epo2_supplier = epo2_supplier;
    }
    public List<epo2_PurchaseOrder> getEpo2_purchaseorders() {
        return epo2_purchaseorders;
    }

    public void addEpo2_purchaseorder(Epo2_purchaseorder epo2_purchaseorder) {
        this.epo2_purchaseorders.add(epo2_purchaseorder);
    }

}