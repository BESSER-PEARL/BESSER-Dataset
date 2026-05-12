





import java.util.List;
import java.util.ArrayList;

public class promotions  {

    private String promotionCode;
    private int startDate;
    private int endDate;



    public promotions(
        String promotionCode,        int startDate,        int endDate    ) {
        this.promotionCode = promotionCode;
        this.startDate = startDate;
        this.endDate = endDate;
    }


    public String getPromotioncode() {
        return promotionCode;
    }

    public void setPromotioncode(String promotionCode) {
        this.promotionCode = promotionCode;
    }
    public int getStartdate() {
        return startDate;
    }

    public void setStartdate(int startDate) {
        this.startDate = startDate;
    }
    public int getEnddate() {
        return endDate;
    }

    public void setEnddate(int endDate) {
        this.endDate = endDate;
    }


}