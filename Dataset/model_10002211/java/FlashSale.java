





import java.util.List;
import java.util.ArrayList;

public class FlashSale  {

    private int DiscountAmount;
    private String FlashSaleName;
    private String Description;
    private int FlashSaleID;
    private int OnlineShopID;
    private int DiscountPercent;





    private BaseDateInformation basedateinformation;




    private OnlineShop onlineshop;


    public FlashSale(
        int DiscountAmount,        String FlashSaleName,        String Description,        int FlashSaleID,        int OnlineShopID,        int DiscountPercent    ) {
        this.DiscountAmount = DiscountAmount;
        this.FlashSaleName = FlashSaleName;
        this.Description = Description;
        this.FlashSaleID = FlashSaleID;
        this.OnlineShopID = OnlineShopID;
        this.DiscountPercent = DiscountPercent;
    }


    public int getDiscountamount() {
        return DiscountAmount;
    }

    public void setDiscountamount(int DiscountAmount) {
        this.DiscountAmount = DiscountAmount;
    }
    public String getFlashsalename() {
        return FlashSaleName;
    }

    public void setFlashsalename(String FlashSaleName) {
        this.FlashSaleName = FlashSaleName;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getFlashsaleid() {
        return FlashSaleID;
    }

    public void setFlashsaleid(int FlashSaleID) {
        this.FlashSaleID = FlashSaleID;
    }
    public int getOnlineshopid() {
        return OnlineShopID;
    }

    public void setOnlineshopid(int OnlineShopID) {
        this.OnlineShopID = OnlineShopID;
    }
    public int getDiscountpercent() {
        return DiscountPercent;
    }

    public void setDiscountpercent(int DiscountPercent) {
        this.DiscountPercent = DiscountPercent;
    }

    public BaseDateInformation getBasedateinformation() {
        return basedateinformation;
    }

    public void setBasedateinformation(BaseDateInformation basedateinformation) {
        this.basedateinformation = basedateinformation;
    }
    public OnlineShop getOnlineshop() {
        return onlineshop;
    }

    public void setOnlineshop(OnlineShop onlineshop) {
        this.onlineshop = onlineshop;
    }

}