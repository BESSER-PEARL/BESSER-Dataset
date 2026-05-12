





import java.util.List;
import java.util.ArrayList;

public class PostStay_Entity  {

    private String DiscountPoints;
    private String PromotionPoints;
    private String ThanksMessage;



    public PostStay_Entity(
        String DiscountPoints,        String PromotionPoints,        String ThanksMessage    ) {
        this.DiscountPoints = DiscountPoints;
        this.PromotionPoints = PromotionPoints;
        this.ThanksMessage = ThanksMessage;
    }


    public String getDiscountpoints() {
        return DiscountPoints;
    }

    public void setDiscountpoints(String DiscountPoints) {
        this.DiscountPoints = DiscountPoints;
    }
    public String getPromotionpoints() {
        return PromotionPoints;
    }

    public void setPromotionpoints(String PromotionPoints) {
        this.PromotionPoints = PromotionPoints;
    }
    public String getThanksmessage() {
        return ThanksMessage;
    }

    public void setThanksmessage(String ThanksMessage) {
        this.ThanksMessage = ThanksMessage;
    }


}