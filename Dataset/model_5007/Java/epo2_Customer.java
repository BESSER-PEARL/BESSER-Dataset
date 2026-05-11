





import java.util.List;
import java.util.ArrayList;

public class epo2_Customer  {

    private int customerID;





    private epo2_Supplier epo2_supplier;


    public epo2_Customer(
        int customerID    ) {
        this.customerID = customerID;
    }


    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }

    public epo2_Supplier getEpo2_supplier() {
        return epo2_supplier;
    }

    public void setEpo2_supplier(epo2_Supplier epo2_supplier) {
        this.epo2_supplier = epo2_supplier;
    }

}