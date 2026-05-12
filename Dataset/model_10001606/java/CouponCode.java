





import java.util.List;
import java.util.ArrayList;

public class CouponCode  {

    private String Code;
    private String ExpiryDate;
    private String UserId;
    private int Discount;



    public CouponCode(
        String Code,        String ExpiryDate,        String UserId,        int Discount    ) {
        this.Code = Code;
        this.ExpiryDate = ExpiryDate;
        this.UserId = UserId;
        this.Discount = Discount;
    }


    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }
    public String getExpirydate() {
        return ExpiryDate;
    }

    public void setExpirydate(String ExpiryDate) {
        this.ExpiryDate = ExpiryDate;
    }
    public String getUserid() {
        return UserId;
    }

    public void setUserid(String UserId) {
        this.UserId = UserId;
    }
    public int getDiscount() {
        return Discount;
    }

    public void setDiscount(int Discount) {
        this.Discount = Discount;
    }


}