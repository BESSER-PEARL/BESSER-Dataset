





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private int LoyaltyID;
    private int Discount;





    private processQuery processquery;


    public Login(
        int LoyaltyID,        int Discount    ) {
        this.LoyaltyID = LoyaltyID;
        this.Discount = Discount;
    }


    public int getLoyaltyid() {
        return LoyaltyID;
    }

    public void setLoyaltyid(int LoyaltyID) {
        this.LoyaltyID = LoyaltyID;
    }
    public int getDiscount() {
        return Discount;
    }

    public void setDiscount(int Discount) {
        this.Discount = Discount;
    }

    public processQuery getProcessquery() {
        return processquery;
    }

    public void setProcessquery(processQuery processquery) {
        this.processquery = processquery;
    }

}