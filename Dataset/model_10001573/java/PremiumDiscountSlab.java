





import java.util.List;
import java.util.ArrayList;

public class PremiumDiscountSlab  {

    private String email;
    private String RadixClient;
    private String log;
    private None PremiumSlab_list_;





    private PurchaseAmountSlab purchaseamountslab;


    public PremiumDiscountSlab(
        String email,        String RadixClient,        String log,        None PremiumSlab_list_    ) {
        this.email = email;
        this.RadixClient = RadixClient;
        this.log = log;
        this.PremiumSlab_list_ = PremiumSlab_list_;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getRadixclient() {
        return RadixClient;
    }

    public void setRadixclient(String RadixClient) {
        this.RadixClient = RadixClient;
    }
    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
    }
    public None getPremiumslab_list_() {
        return PremiumSlab_list_;
    }

    public void setPremiumslab_list_(None PremiumSlab_list_) {
        this.PremiumSlab_list_ = PremiumSlab_list_;
    }

    public PurchaseAmountSlab getPurchaseamountslab() {
        return purchaseamountslab;
    }

    public void setPurchaseamountslab(PurchaseAmountSlab purchaseamountslab) {
        this.purchaseamountslab = purchaseamountslab;
    }

}